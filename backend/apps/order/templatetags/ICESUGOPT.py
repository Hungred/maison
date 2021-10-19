from django import template

register = template.Library()


@register.filter(name='iceopt')
def iceopt(type):
    return {
        '去冰':'去冰',
        '微冰':'微冰',
        '正常冰':'正常冰'
    }[str(type)]

@register.filter(name='sugopt')
def sugopt(type):
    return {
        '無糖':'無糖',
        '微糖':'微糖',
        '正常糖':'正常糖'
    }[str(type)]
