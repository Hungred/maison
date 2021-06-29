import datetime
from datetime import date


from django import template

register = template.Library()

@register.filter
def plus_days(value, days):
    return value + datetime.timedelta(days=days)

@register.filter
def compare_days(value):
    return value
    # if value.date() == datetime.today().date():
    #     return True
    # else:
    #     return False