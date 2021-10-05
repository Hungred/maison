from django.forms import ModelForm
from .models import Worksche
from django import forms
import datetime as dt
class WorkscheForm(ModelForm):
    class Meta:
        model = Worksche
        fields = '__all__'

    def clean(self):
        possible_hour = list(range(1, 25))
        possible_min = list(range(0, 60))
        date = dt.date.today()
        print(date)
        workhour = self.cleaned_data.get('workhour')
        offhour = self.cleaned_data.get('offhour')
        todaysche = Worksche.objects.filter(workdate=self.cleaned_data.get('workdate')).filter(empid=self.cleaned_data.get('empid'))


        if int(workhour) not in possible_hour:
            raise forms.ValidationError('非可能的出勤時間')

        workmin = self.cleaned_data.get('workmin')
        if int(workmin) not in possible_min:
            raise forms.ValidationError('非可能的出勤時間')


        if int(offhour) not in possible_hour:
            raise forms.ValidationError('非可能的退勤時間')

        offmin = self.cleaned_data.get('offmin')
        if int(offmin) not in possible_min:
            raise forms.ValidationError('非可能的退勤時間')

        if int(workhour) > int(offhour):
            raise forms.ValidationError('退勤時間必須晚於出勤時間')

        for sche in todaysche:
            on = sche.workhour
            off = sche.offhour

            if workhour >= on:
                if workhour <= off:
                    raise forms.ValidationError('班表重疊')

            if offhour >= on:
                if offhour <= off:
                    raise forms.ValidationError('班表重疊')

            if workhour <= on:
                if offhour >= off:
                    raise forms.ValidationError('班表重疊')
        return


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')