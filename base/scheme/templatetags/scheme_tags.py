from django import template
from scheme.models import Channels, Equipment, Locations

register = template.Library()

@register.filter
def nds(value):
    equipment = Equipment.objects.all()
    return {'equipment' : equipment}