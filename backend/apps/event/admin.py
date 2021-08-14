from django.contrib import admin

# Register your models here.
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('eventname', 'on_going')

admin.site.register(Events, EventAdmin)