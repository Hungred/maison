from django.contrib import admin
from django.urls import path
from . import views

app_name='reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('reservation_add/', views.addbook, name='add'),
    path('reservation_detail/<int:pk>/', views.detailbook, name='detail'),
    path('reservation_update/<int:pk>/', views.updatebook, name='update'),
    path('reservation_del/<int:pk>/', views.delbook, name='delete'),

]