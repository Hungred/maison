from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import context
# Create your views here.
from .forms import BookForm
from ..order.models import Food

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
    foodA = Food.objects.filter(foodtype='A')
    foodB = Food.objects.filter(foodtype='B')
    foodC = Food.objects.filter(foodtype='C')
    foodD = Food.objects.filter(foodtype='D')

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