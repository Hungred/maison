from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from datetime import date

# Create your views here.



def index(request):
    reservations = Book.objects.all()
    context = {'reservations':reservations, 'time':date.today()}
    return render(request, 'reservation.html', context)

