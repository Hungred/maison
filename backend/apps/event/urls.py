from django.contrib import admin
from django.urls import path
from . import views

app_name='event'
urlpatterns = [
    path('list', views.eventlist, name='index'),
    path('detail/<int:pk>', views.eventdetail, name='detail'),
    path('add/', views.addevent, name='add'),
    path('update/<int:pk>', views.updateevent, name='update'),
    path('delete/<int:pk>', views.delevent, name='delete')

]