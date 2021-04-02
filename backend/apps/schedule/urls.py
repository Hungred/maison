from django.contrib import admin
from django.urls import path
from . import views

app_name='schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('sche_modify/', views.addsche, name='add'),
    path('sche_update/<int:pk>/', views.updatesche, name='update')

]