from django import template

register = template.Library()


@register.filter(name='iceopt')
def iceopt(type):
    return {
        '0':'去冰',
        '1':'微冰',
        '2':'正常冰'
    }[str(type)]

@register.filter(name='sugopt')
def sugopt(type):
    return {
        '0':'無糖',
        '1':'微糖',
        '2':'正常糖'
    }[str(type)]
