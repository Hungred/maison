from django.contrib import admin
from django.urls import path
from . import views

app_name='login'
urlpatterns = [

    path('register', views.sign_up, name='register'),
    path('', views.sign_in, name='index'),
    path('logout', views.log_out, name='logout'),
]