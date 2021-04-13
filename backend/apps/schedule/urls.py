from django.contrib import admin
from django.urls import path
from . import views

app_name='schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('sche_modify/', views.addsche, name='add'),
    path('sche_detail/<int:pk>', views.detailsche, name='detail'),
    path('sche_update/<int:pk>/', views.updatesche, name='update'),
    path('sche_del/<int:pk>/', views.delsche, name='delete'),

]