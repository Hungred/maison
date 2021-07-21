from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context

from .models import Worksche
from ..login.models import Employee_data
from .forms import WorkscheForm
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json
from .forms import DeleteConfirmForm
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, date
from django.utils.timezone import datetime, timedelta
import datetime as dt




@login_required(login_url="login:index")
def index(request):
    worksches = Worksche.objects.all()
    employees = Employee_data.objects.all()
    today = datetime.today()

    #抓出這一周的班表
    date = dt.date.today()
    start_week = date - dt.timedelta(date.weekday())
    end_week = start_week + dt.timedelta(7)
    recent_sche = Worksche.objects.filter(workdate__range=[start_week, end_week])

    #定義要傳到前端的資料串
    week_sche = [{
        'weekday': (i),
        'sche': []
    } for i in range(1, 8)]#加上'empid' 想辦法分類對應班表到對應員工 以員工數為基準 所以weekday要改傳入方式


    #將最近的班表分類到資料串
    for worksche in recent_sche:
        check_day = worksche.workdate.isoweekday()
        for i in range(7):
            if check_day == week_sche[i]['weekday']:
                week_sche[i]['sche'].append(worksche)


        # week_sche['sche'].append(worksche)


    context = {'worksches': worksches, 'employees': employees,
               'today': date, 'weeksche': week_sche,
               'start': start_week}
    return render(request, 'sche.html', context)

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