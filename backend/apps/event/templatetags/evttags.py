from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='True_or_False')
def True_or_False(type):
    return {
            'True': '是',
            'False': '否',
        }[str(type)]