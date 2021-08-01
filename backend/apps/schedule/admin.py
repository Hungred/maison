from django.contrib import admin
from .models import Worksche
from ..order.models import *
# Register your models here.
admin.site.register(Worksche)

admin.site.register(Food)

admin.site.register(ordinfo)
