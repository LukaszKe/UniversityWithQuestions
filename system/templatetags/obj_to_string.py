from django import template
from system.models import University

register = template.Library()
@register.filter
def toString(obj):
    return ' '.join(str(uni) for uni in obj.all())