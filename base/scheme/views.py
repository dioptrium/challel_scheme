
from pyexpat import model
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Channels, Equipment, Locations
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .forms import *
from .models import *
from django.forms import modelformset_factory
from django.urls import reverse

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


class CreateLocationView(CreateView):
    form_class = LocationForm
    template_name = 'scheme/create_location.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateLocationView, self).get_context_data(**kwargs)
        context['equipment_formset'] = EquipmentInlineFormset()
        return context
    
    def post(self,request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        equipment_formset = EquipmentInlineFormset(self.request.POST)
        if form.is_valid() and equipment_formset.is_valid():
            return self.form_valid(form, equipment_formset)
        else:
            return self.form_invalid(form, equipment_formset)
        
    def form_valid(self, form, equipment_formset):
        self.object = form.save(commit=False)
        self.object.save()
        
        equipment_1 =equipment_formset.save(commit=False)
        for eq in equipment_1:
            eq.locations_connect = self.object
            eq.save()
        return redirect(reverse('location:location_list'))
        
    def form_invalid(self, form, equiment_formset):
        return self.render_to_response(
            self.get_context_data(form=form, equiment_formset = equiment_formset)
        )
            

class UpdateLocationView(UpdateView):
  model = Locations
  form_class = LocationForm
  template_name = 'scheme/update_location.html'

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    equipment_formset = EquipmentInlineFormset(instance = self.object)
    return self.render_to_response(self.get_context_data(form = form, equipment_formset = equipment_formset))

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    equipment_formset = EquipmentInlineFormset(self.request.POST, instance=self.object)
    if (form.is_valid() and equipment_formset.is_valid()):
      return self.form_valid(form, equipment_formset)
    return self.form_invalid(form, equipment_formset)

  def form_valid(self, form, equipment_formset):
    self.object = form.save()
    equipment_formset.instance = self.object
    equipment_formset.save()
    return HttpResponseRedirect(self.get_success_url())

  def form_invalid(self, form, equipment_formset):
    return self.render_to_response(self.get_context_data(form=form, equipment_formset=equipment_formset))
   
   
class DeleteLocationView(DeleteView):
    model = Locations
    success_url = '/scheme'
    template_name = 'scheme/delete_location.html'



def CreateChannelView(request):
    locations = Locations.objects.all()
    error=''
    if request.method=='POST':
        form= ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save()
            return redirect (channel)
        else:
            error = 'Mistake'
    form=ChannelForm()
    context = {'form':form, 'error':error, 'locations':locations}
    return render (request, 'scheme/create_channel.html', context)

def CreateEquipmentView(request):
    error=''
    if request.method=='POST':
        form= EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            return redirect (equipment)
        else:
            error = 'Mistake'
    form=EquipmentForm()
    context = {'form':form, 'error':error}
    return render (request, 'scheme/create_equipment.html', context)