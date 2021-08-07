from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date
from django.utils.timezone import datetime, timedelta

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


# class UploadModelForm(forms.ModelForm):
#     class Meta:
#         model = Food
#         fields = ('image',)
#         widgets = {
#             'image': forms.FileInput(attrs={'class': 'form-control-file'})
#         }