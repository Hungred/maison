from django import forms

from ..reservation.models import Book
from django.utils.timezone import datetime

class BookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Book
        
    def clean_booktime(self, *args, **kwargs):
        today = datetime.today()
        bookdate = self.cleaned_data.get('booktime')  # 取得樣板所填寫的資料
        check_day = bookdate.replace(tzinfo=None)
        if (check_day - today).days<=1:
            raise forms.ValidationError('訂位時間不正確')
        if int(bookdate.minute)<30:
            bookdate=bookdate.replace(minute=00)
        elif int(bookdate.minute)>=30:
            bookdate=bookdate.replace(minute=30)
        return bookdate

    def clean_bookadt(self):
        adt = self.cleaned_data.get('bookadt')
        if int(adt)<=0:
            raise forms.ValidationError('至少需有一位大人')
        return adt