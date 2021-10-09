from django.forms import ModelForm
from django import forms

class SalaryForm(forms.Form):
    year = forms.IntegerField(label='年份')
    month = forms.IntegerField(label='月份')
    hourly_rate= forms.IntegerField(label='時薪')