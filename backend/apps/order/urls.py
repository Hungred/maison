from django.contrib import admin
from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('', views.index, name='index'),
    path('orderdetail', views.orderdetail, name='orderdetail'),
]