from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from datetime import date
from django.utils.timezone import datetime, timedelta
# Create your views here.

def index(request):
    today = datetime.today()
    results = [{
        'date': (today + timedelta(days=i)).date(),
        'reservations': []
    } for i in range(4)]#先產出這四天的日期塞到陣列中
    recent_reservations = Book.objects\
        .filter(booktime__range=[today.date(), results[-1]['date']])#從資料庫抓出近四天的預約

    for reservation in recent_reservations:
        check_day = reservation.booktime.replace(tzinfo=None)#把timezone拿掉
        index = (check_day - today).days + 1
        results[index]['reservations'].append(reservation)
    return render(request, 'reservation.html',
                  {'recent_reservations': results})

# def index(request):
#     reservations = Book.objects.all()
#     context = {'reservations':reservations, 'time':date.today()}
#     return render(request, 'reservation.html', context)

