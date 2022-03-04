from ast import Eq
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from scheme.models import Channels, Equipment, Locations, Specifications


class EquipmentOnline(admin.TabularInline):
    model = Equipment

class SpecificationsInline(admin.TabularInline):
    model = Specifications

@admin.register(Locations)
class LocationsAdmin(ModelAdmin):
    '''list_display = ['location','address']
    ordering = ['location']
    search_fields = ['location']'''
    inlines = [EquipmentOnline]


@admin.register(Equipment)
class EquipmentAdmin(ModelAdmin):
    inlines = [SpecificationsInline]
    ordering = ['equipment']
    
    
class Equipment_connectInline(admin.TabularInline):
    model = Channels.equipment_connect.through
    

@admin.register(Channels)
class ChannelsAdmin(ModelAdmin):
    list_display = ['channel_name','object_a', 'object_b'] 
    ordering = ['channel_name']
    search_fields = ['channel_name']
    filter_horizontal = ['equipment_connect']
    inlines = [Equipment_connectInline,]
    exclude = ('equipment_connect',)




