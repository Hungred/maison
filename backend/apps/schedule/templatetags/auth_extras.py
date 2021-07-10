from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

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