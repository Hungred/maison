from django import template
import datetime as dt
register = template.Library()

@register.filter(name='times')
def times(number):
    return range(1,number)

@register.filter(name='to_string')
def to_string(data):
    return str(data)

@register.filter(name='to_cut_string')
def to_cut_string(data):
    cut = str(data)
    return cut[0:4]

@register.filter(name='print')
def print(data):
    return print(data)

@register.filter(name='weekdate')
def weekdate(date, days):
    return date + dt.timedelta(days)

@register.filter(name='to_weekday')
def to_weekday(date):
    return {
            '1': 'Tue',
            '2': 'Wed',
            '3': 'Thu',
            '4': 'Fri',
            '5': 'Sat',
            '6': 'Sun',
        }[str(date)]
