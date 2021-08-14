from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import context
# Create your views here.
from .forms import BookForm
from ..order.models import Food
from ..event.models import Events

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def activity(request):
    events = Events.objects.filter(on_going=True)
    context = {
        'events': events
    }
    return render(request, 'activity1.html', context)

def environment(request):
    return render(request, 'environment.html')
#
def food(request):
    foodA = Food.objects.filter(foodtype='A', on_sales=True)
    foodB = Food.objects.filter(foodtype='B', on_sales=True)
    foodC = Food.objects.filter(foodtype='C', on_sales=True)
    foodD = Food.objects.filter(foodtype='D', on_sales=True)

    context = {
        'foodA': foodA,
        'foodB': foodB,
        'foodC': foodC,
        'foodD': foodD,
    }
    return render(request, 'food.html', context)

def Book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('customer:index')
    return render(request, 'customer/book.html', {'form': form})