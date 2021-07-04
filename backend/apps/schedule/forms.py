from django.forms import ModelForm
from .models import Worksche
from django import forms
class WorkscheForm(ModelForm):
    class Meta:
        model = Worksche
        fields = '__all__'

    def clean(self):
        possible_hour = list(range(1, 25))
        possible_min = list(range(0, 60))
        workhour = self.cleaned_data.get('workhour')
        if int(workhour) not in possible_hour:
            raise forms.ValidationError('非可能的出勤時間')

        workmin = self.cleaned_data.get('workmin')
        if int(workmin) not in possible_min:
            raise forms.ValidationError('非可能的出勤時間')

        offhour = self.cleaned_data.get('offhour')
        if int(offhour) not in possible_hour:
            raise forms.ValidationError('非可能的退勤時間')

        offmin = self.cleaned_data.get('offmin')
        if int(offmin) not in possible_min:
            raise forms.ValidationError('非可能的退勤時間')
        return


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')