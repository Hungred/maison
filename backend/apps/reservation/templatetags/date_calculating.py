import datetime
# from datetime import date
from datetime import datetime as datetime2

from django import template

register = template.Library()

@register.filter
def plus_days(value, days):
    return value + datetime.timedelta(days=days)

@register.filter
def compare_days(value, days):
    comp=plus_days(datetime2.today().date(), days)
    if value.date() == comp:
        print('123')
        return True
    else:
        print('456')
        return None