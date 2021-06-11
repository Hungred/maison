from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import context
# Create your views here.
from .forms import BookForm
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

def Book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('customer:index')
    return render(request, 'customer/book.html', {'form': form})