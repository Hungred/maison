from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Count, F, Sum, Q
from django.http import JsonResponse
from django.db.models.functions import ExtractYear, ExtractMonth

from datetime import datetime, date
from django.utils.timezone import datetime, timedelta
import datetime as dt
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from ..schedule.models import *
from .forms import *
from ..login.models import *
from ..order.models import *
from utils.charts import *


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
def statistics_view(request):
    return render(request, 'statistics.html', {})

@login_required(login_url="login:index")
def product_sales_statistics_view(request):
    context = {}
    return render(request, 'product_sales.html', context)




def get_filter_options(request):
    grouped_purchases = Ord.objects.annotate(year=ExtractYear('ordtime')).values('year').order_by('-year').distinct()

    options = [purchase['year'] for purchase in grouped_purchases]

    return JsonResponse({
        'options': options,
    })


def get_month_options(request):
    grouped_purchases = Ord.objects.annotate(month=ExtractMonth('ordtime')).values('month').order_by('month').distinct()

    options = [purchase['month'] for purchase in grouped_purchases]
    options.append('全年')

    return JsonResponse({
        'options': options,
    })


def Sales(request, year):
    sales = Ord.objects.filter(ordtime__year=year)
    month_sales = sales.annotate(price=F('total_price')).annotate(month=ExtractMonth('ordtime')) \
        .values('month').annotate(total=Sum('total_price')).values('month', 'total').order_by('month')
    sales_dict = get_year_dict()

    for sales in month_sales:
        sales_dict[months[sales['month'] - 1]] = round(sales['total'], 2)

    return JsonResponse({
        'title': f'{year}年每月營收 ',
        'data': {
            'labels': list(sales_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(sales_dict.values()),
            }]
        },
    })


def yearly_product_chart(request, year, month):
    if month == '全年':
        foods = ordinfo.objects.filter(o_id__ordtime__year=year).filter(
            Q(o_id__ordcheck=3) | Q(o_id__ordcheck=2))
    else:
        foods = ordinfo.objects.filter(o_id__ordtime__year=year).filter(o_id__ordtime__month=month).filter(
            Q(o_id__ordcheck=3) | Q(o_id__ordcheck=2))


    food_list = list(Food.objects.values_list('fid', 'foodname').distinct())

    grouped_purchases = foods.values('f_id').annotate(count=Sum('foodq'))

    print(grouped_purchases)

    food_q_dict = dict()

    for food_name in food_list:
        food_q_dict[food_name[1]] = 0

    for group in grouped_purchases:
        food_q_dict[dict(food_list)[group['f_id']]] = group['count']

    return JsonResponse({
        'title': f'{year}/{month} 餐點售出圓餅圖 ',
        'data': {
            'labels': list(food_q_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': generate_color_palette(len(food_q_dict)),
                'borderColor': generate_color_palette(len(food_q_dict)),
                'data': list(food_q_dict.values()),
            }]
        },
    })


@login_required(login_url="login:index")
@group_required('boss', 'manage')
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
