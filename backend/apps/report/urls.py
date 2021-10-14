from django.contrib import admin
from django.urls import path
from . import views

app_name='report'
urlpatterns = [
    path('statistics/', views.statistics_view),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/month-options/', views.get_month_options, name='chart-month-options'),
    path('chart/sales/<int:year>/', views.Sales, name='chart-sales'),
    path('chart/yearly_product_chart/<int:year>/<str:month>/', views.yearly_product_chart, name='chart-payment-method'),
    path('salary', views.salary, name='salary'),
]