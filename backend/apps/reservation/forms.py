from django.forms import ModelForm
from .models import *
from django import forms

class ReservationForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')