from django.contrib import admin
from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('', views.index, name='index'),
    path('pass/<int:serno>', views.pass_to_checked, name='pass'),
    path('orderinfo/<int:pk>', views.orderinfo, name='orderinfo'),
    path('menu_manage', views.menu_index, name='menu'),
    path('fooddetail/<str:fid>', views.fooddetail, name='food_detail'),
    path('foodupdate/<str:fid>', views.updatefood, name='food_update'),
    path('orderdetail', views.orderdetail, name='orderdetail'),
    path('checkout/<str:oid>', views.checkout, name='checkout'),
    path('product', views.product, name='product'),
]