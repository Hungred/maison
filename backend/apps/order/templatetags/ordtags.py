from django import template


register = template.Library()

@register.filter(name='to_foodtype')
def to_foodtype(type):
    return {
            'A': '主餐',
            'B': '副餐',
            'C': '甜點',
            'D': '飲料',
        }[str(type)]

@register.filter(name='True_or_False')
def True_or_False(type):
    return {
            'True': '是',
            'False': '否',
        }[str(type)]
