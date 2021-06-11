from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def activity(request):
    return render(request, 'activity1.html')

def environment(request):
    return render(request, 'environment.html')
#
def food(request):
    return render(request, 'food.html')