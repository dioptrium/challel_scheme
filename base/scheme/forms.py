from ast import Eq
from django import forms
from .models import Channels, Equipment, Locations
from django.forms import formset_factory


class EquipmentForm(forms.ModelForm):
    class Meta:
        model=Equipment
        fields = ['equipment','description','locations_connect']

  

#EquipmentFormSet = formset_factory(EquipmentForm, extra=1)


class ChannelForm(forms.ModelForm):
    #field = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model=Channels
        fields =['channel_name', 'object_a', 'object_b','traffic','description','equipment_connect',]

    i = Equipment.objects.all()
   
    equipment_connect = forms.ModelMultipleChoiceField(queryset=i, widget=forms.CheckboxSelectMultiple)
    locations_connect = Locations.objects.all()

