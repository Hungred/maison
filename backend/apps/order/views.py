from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context
from django.views.decorators.csrf import requires_csrf_token
from django.db.models import Avg, Max, Min, Count, F, Sum, Q
from .models import *
from .forms import *
import base64
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils import timezone
import datetime as dt
from .classes import *


# Create your views here.

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='login:permission_denied')


@login_required(login_url="login:index")
def index(request):
    # 只抓當日
    order = Ord.objects.filter(wid__contains=int(
        str(dt.date.today().year) + str(dt.date.today().month).zfill(2) + str(dt.date.today().day).zfill(2)))

    # 閒置超過10分鐘自動從清單中移除(仍在資料庫中)
    now = timezone.localtime(timezone.now())
    checktime = now - dt.timedelta(minutes=10)
    for ord in order:
        ordtime = ord.ordtime
        if ordtime < checktime:
            if ord.ordcheck < 2:
                ord.ordcheck = 3
                ord.save()

    # 抓出未結帳訂單
    handling = order.filter(ordcheck=1)
    # 定義要傳到前端的資料串
    handling2 = [{
        'no': (i),
        'order': []
    } for i in range(len(handling))]
    # 將資料分類到資料串
    for i in range(len(handling)):
        handling2[i]['order'].append(handling[i])

    checked = order.filter(ordcheck=2)
    checked2 = [{
        'no': (i),
        'order': []
    } for i in range(len(checked))]
    for i in range(len(checked)):
        checked2[i]['order'].append(checked[i])

    context = {
        'order': order,
        'handling': handling2,
        'checked': checked2,
    }
    return render(request, 'order.html', context)


@login_required
@group_required('manage', 'boss', 'employee')
def pass_to_checked(request, serno):
    print(serno)
    ord = Ord.objects.get(serno=serno)
    ord.ordcheck = 2
    ord.save()
    return redirect('order:index')


@login_required
@group_required('manage', 'boss')
def menu_index(request):
    # 主餐
    As = Food.objects.filter(foodtype='A')
    halfA = int(As.count() / 2)
    # 副餐
    Bs = Food.objects.filter(foodtype='B')
    halfB = int(Bs.count() / 2)
    # 甜點
    Cs = Food.objects.filter(foodtype='C')
    halfC = int(Cs.count() / 2)
    # 飲料
    Ds = Food.objects.filter(foodtype='D')
    halfD = int(Ds.count() / 2)
    # 上架中
    Os = Food.objects.filter(on_sales=True)
    halfO = int(Os.count() / 2)
    # 未上架
    Xs = Food.objects.filter(on_sales=False)
    halfX = int(Xs.count() / 2)

    context = {
        'As_2': As[0:halfA], 'As_1': As[halfA:],
        'Bs_2': Bs[0:halfB], 'Bs_1': Bs[halfB:],
        'Cs_2': Cs[0:halfC], 'Cs_1': Cs[halfC:],
        'Ds_2': Ds[0:halfD], 'Ds_1': Ds[halfD:],
        'Os_2': Os[0:halfO], 'Os_1': Os[halfO:],
        'Xs_2': Xs[0:halfX], 'Xs_1': Xs[halfX:],

    }
    return render(request, 'manage/menu.html', context)


def SearchPage(request):
    srh = request.GET['query']

    foods = Food.objects.filter(foodname__icontains=srh)

    if not foods:
        foods = Food.objects.filter(fid__icontains=srh)

    if not foods:
        foods = Food.objects.filter(foodprice__icontains=srh)

    half = int(foods.count() / 2)

    params = {'foods_2': foods[0:half], 'foods_1': foods[half:], 'search': srh}
    return render(request, 'manage/search_page.html', params)


@group_required('manage', 'boss')
@login_required(login_url="login:index")
def fooddetail(request, fid):
    food = get_object_or_404(Food, fid=fid)

    context = {
        'food': food,
    }
    return render(request, 'manage/food_detail.html', context)


@group_required('manage', 'boss')
@permission_required('order.add_food', raise_exception=True)
def addfood(request):
    form = FoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, '新增成功')
            return redirect('order:menu')
        except Exception:
            messages.error(request, '請確認資料無誤')
            return redirect('order:menu')
    return render(request,
                  'manage/food_add.html',
                  {'form': form},
                  )


@group_required('manage', 'boss')
@permission_required('order.change_food', raise_exception=True)
def updatefood(request, fid):
    food = Food.objects.get(fid=fid)
    form = FoodForm(request.POST or None, instance=food)
    if request.method == 'POST':
        form = FoodForm(request.POST or None, request.FILES or None, instance=food)

    if form.is_valid():
        form.save()
        messages.success(request, '修改成功')
        return redirect('order:menu')
    return render(request, 'manage/food_update.html', {'form': form})


@group_required('manage', 'boss')
@permission_required('order.delete_food', raise_exception=True)
def delfood(request, fid):
    food = get_object_or_404(Food, fid=fid)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        food.delete()
        return redirect('order:menu')
    return render(request, 'manage/food_del.html', {'form': form})


# 後台訂單詳細資料
@login_required(login_url="login:index")
def orderinfo(request, pk):
    order = get_object_or_404(Ord, serno=pk)
    order0 = ordinfo.objects.filter(o_id__wid__contains=order.wid)

    order_list = [{
        'no': (i),
        'food': [],
        'tip': [],
    } for i in range(0, len(order0))]

    for i in range(0, len(order0)):
        order_list[i]['food'].append(order0[i])

    context = {
        'order': order,
        'order_list': order_list,
    }
    return render(request, 'orderinfo.html', context)

@login_required
@group_required('manage', 'boss', 'employee')
def pass_to_abandon(request, serno):
    ord = Ord.objects.get(serno=serno)
    ord.ordcheck = 3
    ord.save()
    return redirect('order:index')

def orderdetail(request, oid):
    try:
        decodedBytes = base64.b64decode(oid)
        decoded_order_id = str(decodedBytes, "utf-8")
    except:
        return redirect("/order/product")

    split=decoded_order_id.split("DET")
    order_id=split[1]
    food = Food.objects.all()
    ord = Ord.objects.get(wid__contains=order_id)
    order_status = ord.ordcheck
    if order_status != 1:
        return redirect("/order/product")
    orderinfo = ordinfo.objects.filter(o_id__wid__contains=order_id)
    context = {
        'food': food,
        'ord': ord,
        'orderinfo': orderinfo,

    }
    return render(request, 'orderdetail.html', context)

def feedback(request):
    try:
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('order:product')
        return render(request, 'feedbacks.html', {'form': form})
    except:
        return redirect("/order/product")


def checkout(request, oid):
    try:
        decodedBytes = base64.b64decode(oid)
        decoded_order_id = str(decodedBytes, "utf-8")
    except:
        return redirect("/order/product")
    if request.method == "GET":
        orid = ordinfo.objects.filter(o_id__wid__contains=decoded_order_id)
        if not orid:
            return redirect("/order/product")
        order = Ord.objects.get(wid=decoded_order_id)
        order_status = order.ordcheck
        if order_status != 0:
            return redirect("/order/product")
        total_price = order.total_price

        params = {'oid': orid, 'total_price': total_price}

        return render(request, 'checkout.html', params)
    elif request.method == "POST":
        cartitems = []
        orid = ordinfo.objects.filter(o_id__wid__contains=decoded_order_id)
        for orders in orid:
            cartitem = {"foodid": orders.f_id.fid, "foodAmount": orders.foodq, "ice": orders.ordice,
                        "sug": orders.ordsua, "tip": orders.ordtip, "unique_id": orders.unique_id}
            cartitems.append(cartitem)
        return JsonResponse(cartitems, safe=False)


def checkoutconfirmed(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = Ord.objects.get(wid=order_id)

        total_price = 0
        orid = ordinfo.objects.filter(o_id__wid__contains=order_id)
        # orid.delete()
        cart = json.loads(request.POST.get('cart'))

        for food in cart:
            curFood = Food.objects.get(pk=food['foodid'])
            price = curFood.foodprice
            sum_price = price * food['foodAmount']

            total_price += sum_price

            curOrd = orid.filter(f_id__fid__contains=food['foodid']).filter(unique_id=food['unique_id'])
            curOrd.update(
                foodq=food['foodAmount'],
                foodp=sum_price,
                ordice=food['ice'],
                ordsua=food['sug'],
                ordtip=food['tip']
            )
            # curOrd.save()
            order.total_price = total_price
            order.tabnum=request.POST.get('tabnum')
            order.ordcheck = 1
            order.save()
        detailid="DET"+order_id
        encodedBytes = base64.b64encode(detailid.encode("utf-8"))
        encoded_order_id = str(encodedBytes, "utf-8")
        return HttpResponse(json.dumps({
            'order_id': encoded_order_id
        }))


def foodlist(request):
    if request.method == "POST":
        food = Food.objects.all()
        foodlist = []
        for foods in food:
            if foods.on_sales:
                fooddict = {"foodid": foods.fid, "foodname": foods.foodname, "foodPrice": foods.foodprice,
                            "foodImg": foods.image.url}
                foodlist.append(fooddict)
        return JsonResponse(foodlist, safe=False)
        # return HttpResponse(json.dumps({
        #     'foodlist': foodlist
        # }))


@requires_csrf_token
def product(request):
    if request.method == "GET":
        food = Food.objects.all()
        ord = Ord.objects.all()

        context = {
            'food': food,
            'ord': ord,
        }
        return render(request, 'product.html', context)
    elif request.method == "POST":
        cart = json.loads(request.POST.get('cart'))
        new_order = Ord(ordcheck=0)
        new_order.save()
        order_id = new_order.wid
        total_price = 0
        unique_id=0
        for food in cart:
            curFood = Food.objects.get(pk=food['foodid'])
            price = curFood.foodprice
            sum_price = price * food['foodAmount']

            total_price += sum_price
            unique_id+=1
            ordinfo.objects.create(
                o_id=new_order,
                f_id=curFood,
                unique_id=unique_id,
                foodq=food['foodAmount'],
                foodp=sum_price,
                ordice=food['ice'],
                ordsua=food['sug'],
                ordtip=food['tip']
            )
            new_order.total_price = total_price
            new_order.save()

        encodedBytes = base64.b64encode(order_id.encode("utf-8"))
        encoded_order_id = str(encodedBytes, "utf-8")
        return HttpResponse(json.dumps({
            'order_id': encoded_order_id
        }))
