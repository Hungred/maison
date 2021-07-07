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
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="login:index")
def index(request):
    worksches = Worksche.objects.all()
    return render(request, 'sche.html', {'worksches':worksches})

def get_user(request):
    user = User.objects.all()
    return render(request, 'sche.html', {'user':user})

@login_required(login_url="login:index")
def detailsche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    return render(request, 'sche_detail.html', {'worksche': worksche})

@permission_required('schedule.add_worksche', raise_exception=True)
def addsche(request):
    form = WorkscheForm(request.POST or None)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, '新增成功')
            return redirect('schedule:index')
        except Exception:
            messages.error(request, '請確認資料無誤')
            return redirect('schedule:index')
    return render(request,
                  'sche_modify.html',
                  {'form':form},
                  )

@permission_required('schedule.change_worksche', raise_exception=True)
def updatesche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    form = WorkscheForm(request.POST or None, instance=worksche)
    if form.is_valid():
        form.save()
        return redirect('schedule:index')
    return render(request, 'sche_update.html', {'form':form})

@permission_required('schedule.delete_worksche', raise_exception=True)
def delsche(request, pk):
    worksche = get_object_or_404(Worksche, serno=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        worksche.delete()

        return redirect('schedule:index')
    return render(request, 'sche_del.html', {'form': form})