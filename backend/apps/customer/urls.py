from django.contrib import admin
from django.urls import path
from . import views
app_name='customer'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.Book, name='book'),
]