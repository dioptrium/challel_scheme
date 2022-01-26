from django.urls import path 
from . import views 
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    path('locations', permission_required('scheme.view_locations')(views.LocationsView), name='url_locations'),
    
]
