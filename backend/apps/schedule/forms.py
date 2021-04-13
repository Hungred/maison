from django.forms import ModelForm
from .models import Worksche
from django import forms
class WorkscheForm(ModelForm):
    class Meta:
        model = Worksche
        fields = '__all__'

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')