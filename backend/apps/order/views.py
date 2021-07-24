from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context
from django.views.decorators.csrf import requires_csrf_token

from .models import *

from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login:index")
def index(request):
    order = Ord.objects.all()
    return render(request, 'order.html', {'order':order})

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

def checkout(request):
    return render(request, 'checkout.html')

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
        food_amount=0;
        total_price =0
        for food in cart:
            curFood = Food.objects.get(pk=food)
            price = curFood.foodprice
            food_amount+=1
            total_price+=price

            ordinfo.objects.create(
                o_id=new_order,
                f_id=curFood,
                foodq=food_amount,
            )

        return HttpResponse(json.dumps({
            'order_id': order_id
        }))


