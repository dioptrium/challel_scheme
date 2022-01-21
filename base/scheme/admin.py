from ast import Eq
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from scheme.models import Channels, Equipment, Locations


class EquipmentOnline(admin.TabularInline):
    model = Equipment

@admin.register(Locations)
class LocationsAdmin(ModelAdmin):
    '''list_display = ['location','address']
    ordering = ['location']
    search_fields = ['location']'''
    inlines = [EquipmentOnline]


@admin.register(Equipment)
class EquipmentAdmin(ModelAdmin):
    '''list_display = ['equipment','description'] 
    ordering = ['equipment']
    search_fields = ['equipment']'''
    pass
    
class Equipment_connectInline(admin.TabularInline):
    model = Channels.equipment_connect.through

@admin.register(Channels)
class ChannelsAdmin(ModelAdmin):
    list_display = ['channel_name','object_a', 'object_b', 'location'] 
    ordering = ['channel_name']
    search_fields = ['channel_name']
    #filter_horizontal = ['equipment_connect']
    inlines = [Equipment_connectInline,]
    exclude = ('equipment_connect',)

class PersonForm(forms.ModelForm):
    extra_field = forms.FileInput()
    class Meta:
        model = Channels
        fields = '__all__'



