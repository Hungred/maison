from django.contrib import admin
from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('', views.index, name='index'),
    path('pass/<int:serno>', views.pass_to_checked, name='pass'),
    path('orderdetail', views.orderdetail, name='orderdetail'),
    path('checkout/<str:oid>', views.checkout, name='checkout'),
    path('product', views.product, name='product'),
]