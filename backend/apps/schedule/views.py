from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context

from .models import Worksche
from .forms import WorkscheForm
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json
from .forms import DeleteConfirmForm
def index(request):
    worksches = Worksche.objects.all()
    return render(request, 'sche.html', {'worksches':worksches})

def detailsche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    return render(request, 'sche_detail.html', {'worksche': worksche})

def addsche(request):
    form = WorkscheForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('schedule:index')
    return render(request,
                  'sche_modify.html',
                  {'form':form},
                  )

def updatesche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    form = WorkscheForm(request.POST or None, instance=worksche)
    if form.is_valid():
        form.save()
        return redirect('schedule:index')
    return render(request, 'sche_update.html', {'form':form})

def delsche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        worksche.delete()
        messages.success(request, '刪除成功')
        return redirect('schedule:index')
    return render(request, 'sche_del.html', {'form': form})