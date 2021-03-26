from django.contrib import admin
from .models import Employee, Worksche
from ..order.models import *
# Register your models here.
admin.site.register(Worksche)
admin.site.register(Employee)
admin.site.register(Food)
admin.site.register(Ord)
admin.site.register(ordinfo)
