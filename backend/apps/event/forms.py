from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date
from django.utils.timezone import datetime, timedelta

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')

