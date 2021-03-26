from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.template import context

from .models import Worksche
from .forms import WorkscheForm
from django.contrib import messages

def index(request):
    coffees = Worksche.objects.all()
    return render(request, 'sche.html', {'coffees':coffees})

# def addsche(request):
#     form = WorkscheForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, '新增成功')
#         return redirect('sche')
#     return render(request,
#                   'sche_modify.html',
#                   {'form':form},
#                   )