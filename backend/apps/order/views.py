from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context

from .models import Ord, Food
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
    return render(request, 'orderdetail.html', {'food':food})