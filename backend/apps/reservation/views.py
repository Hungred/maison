from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import context
from .models import *
from .forms import *
from datetime import date
from django.utils.timezone import datetime, timedelta
from django.contrib.auth.decorators import login_required, permission_required


from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json


# Create your views here.

@login_required(login_url="login:index")
def index(request):
    reservations = Book.objects.all()

    today = datetime.today()
    results = [{
        'date': (today + timedelta(days=i)).date(),
        'reservations': []
    } for i in range(5)]#先產出這四天的日期塞到陣列中
    recent_reservations = Book.objects\
        .filter(booktime__range=[today.date(), results[-1]['date']])#從資料庫抓出近四天的預約
    print(recent_reservations)

    for reservation in recent_reservations:
        check_day = reservation.booktime.replace(tzinfo=None)#把timezone拿掉
        index = (check_day - today).days + 1
        results[index]['reservations'].append(reservation)

    print(results)
    del(results[-1])

    context = {'reservations':reservations, 'recent_reservations': results}
    return render(request, 'reservation.html', context)

def get_user(request):
    user = User.objects.all()
    return render(request, 'sche.html', {'user':user})

@login_required(login_url="login:index")
def detailbook(request, pk):
    book = get_object_or_404(Book, serno=pk)
    return render(request, 'reservation_detail.html', {'book':book})

@permission_required('reservation.add_book', raise_exception=True)
def addbook(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
    
        return redirect('reservation:index')
    return render(request,
                  'reservation_new.html',
                  {'form':form},
                  )

@permission_required('reservation.change_book', raise_exception=True)
def updatebook(request, pk):
    book = get_object_or_404(Book, serno=pk)
    form = ReservationForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('reservation:index')
    return render(request, 'reservation_update.html', {'form':form})

@permission_required('reservation.delete_book', raise_exception=True)
def delbook(request, pk):
    book = get_object_or_404(Book, serno=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()

        return redirect('reservation:index')
    return render(request, 'reservation_del.html', {'form': form})

# def index(request):
#     reservations = Book.objects.all()
#     context = {'reservations':reservations, 'time':date.today()}
#     return render(request, 'reservation.html', context)

