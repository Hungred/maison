from django.contrib import admin
from django.urls import path
from . import views

app_name='feedback'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('search/', views.SearchPage, name='search_result'),
]