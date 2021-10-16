from django import template


register = template.Library()

@register.filter(name='topos')
def topos(id):

    return{
            'B': '老闆',
            'M': '管理人員',
            'E': '一般員工',
        }[str(id)]

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)