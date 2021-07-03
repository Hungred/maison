from django.contrib import admin
from .models import Book, Wt
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'booktime')

admin.site.register(Book, BookAdmin)
admin.site.register(Wt)
