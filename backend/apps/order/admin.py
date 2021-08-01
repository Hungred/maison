from django.contrib import admin
from .models import *


class OrdAdmin(admin.ModelAdmin):
    list_display = ('wid', 'ordtime', 'changetime', 'ordcheck', 'tabnum', 'total_price')

admin.site.register(Ord, OrdAdmin)
# Register your models here.

