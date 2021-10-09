from django import template


register = template.Library()

@register.filter(name='topos')
def topos(id):

    return{
            'B': '老闆',
            'M': '管理人員',
            'E': '一般員工',
        }[str(id)]