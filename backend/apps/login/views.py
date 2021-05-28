from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django import template
from .models import Employee_data
from django.db.models import ProtectedError
# Create your views here.

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:index')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('schedule:index')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

@login_required(login_url="login:index")
def log_out(request):
    logout(request)
    return redirect('login:index') #重新導向到登入畫面

@login_required(login_url="login:index")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change.html', {
        'form': form
    })

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})

@login_required
def update_pf(request, username):
    user = get_object_or_404(User, username=username)
    form = UpdateProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('schedule:index')
    return render(request, 'update_pf.html', {'form':form})

def emp_list(request):
    emps = Employee_data.objects.all()
    return render(request, 'employee/emp_list.html', {'emps': emps})

@permission_required('login.add_employee_data', raise_exception=True)
def active_emp(request):
    form = ActiveEmpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('schedule:index')
    return render(request,
                  'active_emp.html',
                  {'form':form},
                  )

@permission_required('login.change_employee_data', raise_exception=True)
def update_emp(request, pk):
    emp = get_object_or_404(Employee_data, pk=pk)
    form = ActiveEmpForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('schedule:index')
    return render(request, 'employee/update_emp.html', {'form':form})

@permission_required('login.delete_employee_data', raise_exception=True) #如果無法刪除如何導向?
def delete_emp(request, pk):
    emp = get_object_or_404(Employee_data, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        try:
            emp.delete()
            messages.success(request, '刪除成功')
            return redirect('schedule:index')
        except ProtectedError as res:
            messages.error(request, '刪除失敗')
            return redirect('schedule:index')
        except Exception as e:
            print(e)

    return render(request, 'employee/delete_emp.html', {'form': form})