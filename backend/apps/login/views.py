from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django import template
from .models import Employee_data
from django.contrib.auth.models import Group
from django.db.models import ProtectedError
# Create your views here.

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:index')
        else:
            messages.error(request, '請修正以下錯誤')
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
        else:
            messages.error(request, '查無使用者或密碼錯誤!')
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
            messages.success(request, '密碼更新成功!')
            return redirect('login:index')
        else:
            messages.error(request, '請修正以下錯誤')
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



def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='login:permission_denied')

@login_required
@group_required('boss')
def emp_list(request):
    emps = Employee_data.objects.all()
    return render(request, 'employee/emp_list.html', {'emps': emps})

@login_required
def permission_denied(request):
    return render(request, 'employee/permission_denied.html')


@login_required
@group_required('boss')
def active_management(request, user):
    group = Group.objects.get(id=2)
    userid = User.objects.get(username=user).pk
    group.user_set.add(userid)
    return render(request, 'employee/active_management.html')

@login_required
@group_required('boss')
def remove_management(request, user):
    group = Group.objects.get(id=2)
    userid = User.objects.get(username=user).pk
    group.user_set.remove(userid)
    return render(request, 'employee/remove_management.html')

@permission_required('login.add_employee_data', raise_exception=True)
def active_emp(request):
    form = ActiveEmpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('login:emp_list')
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
        messages.success(request, '修改成功')
        return redirect('login:emp_list')
    return render(request, 'employee/update_emp.html', {'form':form})

@permission_required('login.delete_employee_data', raise_exception=True) #如果無法刪除如何導向?
def delete_emp(request, pk):
    emp = get_object_or_404(Employee_data, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        try:
            emp.delete()
            messages.success(request, '刪除成功')
            return redirect('login:emp_list')
        except ProtectedError as res:
            messages.error(request, '刪除失敗,因該員工在班表上留有出勤紀錄')
            return redirect('schedule:index')
        except Exception as e:
            print(e)

    return render(request, 'employee/delete_emp.html', {'form': form})