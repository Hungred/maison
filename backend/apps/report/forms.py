from django.forms import ModelForm
from django import forms
from .choices import *

class SalaryForm(forms.Form):
    year = forms.IntegerField(label='年份')
    month = forms.IntegerField(label='月份')
    hourly_rate = forms.IntegerField(label='時薪')

class ProductForm(forms.Form):
    year = forms.IntegerField(label='年份')
    month = forms.TypedChoiceField(choices=MONTH_CHOICES, label='月份')