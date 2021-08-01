from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context
from django.views.decorators.csrf import requires_csrf_token

from .models import *
import base64
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils import timezone
import datetime as dt


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
    #只抓當日
    order = Ord.objects.filter(wid__contains=int(str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2)))

    # 閒置超過10分鐘自動從清單中移除(仍在資料庫中)
    now = timezone.localtime(timezone.now())
    checktime = now - dt.timedelta(minutes=10)
    for ord in order:
        ordtime = ord.ordtime
        if ordtime < checktime:
            if ord.ordcheck != 1:
                ord.ordcheck = 2
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


def orderdetail(request):
    food = Food.objects.all()
    ord = Ord.objects.all()
    orderinfo = ordinfo.objects.all()
    context = {
        'food': food,
        'ord': ord,
        'orderinfo': orderinfo,

    }
    return render(request, 'orderdetail.html', context)


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
        i = 1;

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
        for food in cart:
            curFood = Food.objects.get(pk=food)
            price = curFood.foodprice
            total_price += price

            ordinfo.objects.create(
                o_id=new_order,
                f_id=curFood,
                foodq=1,
            )
            new_order.total_price = total_price
            new_order.save()

        encodedBytes = base64.b64encode(order_id.encode("utf-8"))
        encoded_order_id = str(encodedBytes, "utf-8")
        return HttpResponse(json.dumps({
            'order_id': encoded_order_id
        }))
