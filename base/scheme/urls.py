from django.urls import path 
from . import views 
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    path('equipment', permission_required('scheme.view_equipment')(views.EquipmentView), name='url_equipment'),
    path('<int:pk>/equipment_detail_view', permission_required('scheme.view_equipment')(views.EquipmentDetailView.as_view()), name='url_equipment_detail_view'),
    path('create_equipment', permission_required('scheme.add_equipment')(views.CreateEquipmentView), name='url_create_equipment'),
    path('<int:pk>/update_equipment', permission_required('scheme.change_equipment')(views.UpdateEquipmentView.as_view()), name= 'url_update_equipment'),
    
    path('locations', permission_required('scheme.view_locations')(views.LocationsView), name='url_locations'),
    path('<int:pk>/location_detail_view', permission_required('scheme.view_locations')(views.LocationDetailView.as_view()), name='url_location_detail_view'),
    path('create_location', permission_required('scheme.add_location')(views.CreateLocationView.as_view()), name='url_create_location'),
    path('<int:pk>/update_location', permission_required('scheme.change_locations')(views.UpdateLocationView.as_view()), name= 'url_update_location'),
    path('<int:pk>/delete_location', permission_required('scheme.delete_locations')(views.DeleteLocationView.as_view()), name='url_delete_location'),
    
    path('channels', permission_required('scheme.view_channels')(views.ChannelsView), name='url_channels'),
    path('<int:pk>/channel_detail_view', permission_required('scheme.view_channels')(views.ChannelDetailView.as_view()), name='url_channel_detail_view'),
    path('create_channel', permission_required('scheme.add_channels')(views.CreateChannelView), name='url_create_channel'),
    path('<int:pk>/update_channel', permission_required('scheme.change_сhannels')(views.UpdateChannelView.as_view()), name= 'url_update_channel'),
] 
