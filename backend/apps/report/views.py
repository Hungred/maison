from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg, Max, Min
from django.db.models.functions import ExtractYear, ExtractMonth

from datetime import datetime, date
from django.utils.timezone import datetime, timedelta
import datetime as dt


from ..schedule.models import *
from .forms import *
from ..login.models import *
# Create your views here.

def index(request):
    return HttpResponse('報表')

def salary(request):

    emp_list = Worksche.objects.values('empid', 'empid__empname', 'empid__empid', 'empid__position').distinct()

    salary_list = [{
        'no': (i),
        'emp': [],
        'salary': [],
    } for i in range(0, len(emp_list))]

    for i in range(0, len(emp_list)):
        salary_list[i]['emp'].append(emp_list[i])

    form = SalaryForm(request.POST or None)
    if form.is_valid():

        year = int(form['year'].value())
        month = int(form['month'].value())
        hourlyrate = int(form['hourly_rate'].value())
        this_month_sche = Worksche.objects.filter(workdate__year=year).filter(workdate__month=month)


        for count, emp in enumerate(emp_list):
            check_emp = int(emp.get('empid'))
            hours = 0

            for now in this_month_sche.filter(empid=check_emp):
                on_hour = int(now.workhour)
                off_hour = int(now.offhour)
                on_min = int(now.workmin)
                off_min = int(now.offmin)

                if on_min == off_min:
                    hours += off_hour - on_hour
                if on_min > off_min:
                    hours += off_hour - on_hour - 0.5
                if on_min < off_min:
                    hours += off_hour - on_hour + 0.5

            salary_list[count]['salary'].append(hours * hourlyrate)



    context = {'form': form, 'salary_list': salary_list, }
    return render(request, 'salary.html', context)