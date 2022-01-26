from django.shortcuts import render
from .models import Channels, Equipment, Locations


def LocationsView(request):
    locations = Locations.objects.all()
    context_object_name = 'locations'
    return render (request, 'scheme/locations.html',{'locations': locations})

