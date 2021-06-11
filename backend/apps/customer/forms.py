from django import forms

from ..reservation.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Book