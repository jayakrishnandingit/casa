from django import template
from home.models import MenuItem

register = template.Library()


@register.inclusion_tag('home/partials/snippets/_menu_item.html', takes_context=True)
def menu_items(context):
    return {
        'items': MenuItem.objects.order_by('position').all(),
        'request': context['request'],
    }
