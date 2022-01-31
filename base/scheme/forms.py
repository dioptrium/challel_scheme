from django import forms
from .models import Channels, Equipment


class ChannelForm(forms.ModelForm):
    class Meta:
        model=Channels
        fields ="__all__"
        #['channel_name', 'object_a', 'object_b','traffic','description','equipment_connect',]


    #equipment_connect = forms.ModelMultipleChoiceField(queryset=Equipment.objects.all(),
     #   widget=forms.CheckboxSelectMultiple)