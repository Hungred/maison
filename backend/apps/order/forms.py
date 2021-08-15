from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date
from django.utils.timezone import datetime, timedelta

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')

