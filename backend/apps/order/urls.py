from django.contrib import admin
from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('', views.index, name='index'),
    path('pass/<int:serno>', views.pass_to_checked, name='pass'),
    path('orderinfo/<int:pk>', views.orderinfo, name='orderinfo'),
    path('menu_manage', views.menu_index, name='menu'),
    path('search_result', views.SearchPage, name='search_result'),
    path('fooddetail/<str:fid>', views.fooddetail, name='food_detail'),
    path('foodadd', views.addfood, name='food_add'),
    path('foodupdate/<str:fid>', views.updatefood, name='food_update'),
    path('fooddelete/<str:fid>', views.delfood, name='food_delete'),
    path('orderdetail', views.orderdetail, name='orderdetail'),
    path('checkout/<str:oid>', views.checkout, name='checkout'),
    path('checkout/confirmed/', views.checkoutconfirmed, name='checkoutconfirmed'),
    path('product', views.product, name='product'),
]