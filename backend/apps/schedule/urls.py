from django.contrib import admin
from django.urls import path
from . import views

app_name='schedule'
urlpatterns = [
    path('', views.index),
    path('sche_modify/', views.addsche),

]