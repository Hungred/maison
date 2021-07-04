from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date
from django.utils.timezone import datetime, timedelta

class ReservationForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_booktime(self, *args, **kwargs):
        today = datetime.today()
        bookdate = self.cleaned_data.get('booktime')  # 取得樣板所填寫的資料
        check_day = bookdate.replace(tzinfo=None)
        print((check_day - today).days)
        if (check_day - today).days<=1:
            raise forms.ValidationError('訂位時間不正確')
        return bookdate

    def clean_bookadt(self):
        adt = self.cleaned_data.get('bookadt')
        if int(adt)<=0:
            raise forms.ValidationError('至少需有一位大人')
        return adt

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')