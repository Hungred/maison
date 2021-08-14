from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
# Create your views here.

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='login:permission_denied')

@group_required('manage', 'boss')
@login_required(login_url="login:index")
def eventlist(request):
    events = Events.objects.all()

    context = {
        'events': events
    }
    return render(request, 'event_index.html', context)

@group_required('manage', 'boss')
@login_required(login_url="login:index")
def eventdetail(request, pk):
    event = get_object_or_404(Events, pk=pk)

    context = {
        'event': event,
        }
    return render(request, 'event_detail.html', context)

@group_required('manage', 'boss')
@permission_required('event.add_events', raise_exception=True)
def addevent(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, '新增成功')
            return redirect('event:index')
        except Exception:
            messages.error(request, '新增失敗, 請確認資料無誤')
            return redirect('event:index')
    return render(request,
                  'event_add.html',
                  {'form': form},
                  )

@group_required('manage', 'boss')
@permission_required('order.change_food', raise_exception=True)
def updateevent(request, pk):
    event = Events.objects.get(pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST or None, request.FILES or None, instance=event)

    if form.is_valid():
        form.save()
        messages.success(request, '修改成功')
        return redirect('event:index')
    return render(request, 'event_update.html', {'form': form})

@group_required('manage', 'boss')
@permission_required('order.delete_food', raise_exception=True)
def delevent(request, pk):
    event = get_object_or_404(Events, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        event.delete()
        return redirect('event:index')
    return render(request, 'event_del.html', {'form': form})