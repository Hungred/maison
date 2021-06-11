from django.contrib import admin
from django.urls import path
from . import views

app_name='customer'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('activity', views.activity, name='activity'),
    path('environment', views.environment, name='environment'),
    path('food', views.food, name='food'),
]