import re
from urllib import request
from django.shortcuts import render, redirect
from .models import Channels, Equipment, Locations
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .forms import *


def LocationsView(request):
    locations = Locations.objects.all()
    context_object_name = 'locations'
    return render (request, 'scheme/locations.html',{'locations': locations})

class LocationDetailView(DetailView):
    model = Locations
    template_name = 'scheme/location_detail_view.html'
    context_object_name = 'location_detail'

def ChannelsView(request):
    channels= Channels.objects.all()
    context_object_name = 'channels'
    return render (request, 'scheme/channels.html',{'channels': channels})

class ChannelDetailView(DetailView):
    model = Channels
    template_name = 'scheme/channel_detail_view.html'
    context_object_name = 'channel_detail'

def CreateChannelView(request):
    error=''
    if request.method=='POST':
        form= ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save()
            return redirect (channel)
        else:
            error = 'Mistake'
    form=ChannelForm()
    context = {'form':form, 'error':error}
    return render (request, 'scheme/create_channel.html', context)