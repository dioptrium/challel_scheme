from django.urls import path 
from . import views 
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    path('locations', permission_required('scheme.view_locations')(views.LocationsView), name='url_locations'),
    path('<int:pk>/location_detail_view', permission_required('scheme.view_locationdetailview')(views.LocationDetailView.as_view()), name='url_location_detail_view'),
    path('channels', permission_required('scheme.view_channels')(views.ChannelsView), name='url_channels'),
    path('<int:pk>/channel_detail_view', permission_required('scheme.view_channeldetailview')(views.ChannelDetailView.as_view()), name='url_channel_detail_view'),
    path('create_channel', permission_required('scheme.add_channel')(views.CreateChannelView), name='url_create_channel'),
    path('create_equipment', permission_required('scheme.add_equipment')(views.CreateEquipmentView), name='url_create_equipment'),
    
]
