from django.contrib import admin
from django.urls import path
from . import views

app_name='report'
urlpatterns = [
    path('', views.index),
    path('salary', views.salary, name='salary'),
]