from django import template
from home.models import Skills

register = template.Library()


@register.inclusion_tag('home/partials/snippets/_skills.html', takes_context=True)
def skills(context):
    return {
        'skills': Skills.objects.select_related('category').all(),
        'request': context['request'],
    }
