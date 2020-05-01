from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.geos import Point

from api.models import District, DistrictEditor, State, Service, ServiceChangeRequest, ServiceType
from api.helpers.admin import WGS84_to_Google, location
# Register your models here.

@admin.register(State)
class StateAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', location)
    search_fields = ('name',)
    default_lon, default_lat = WGS84_to_Google(20.5937, 78.9629)

@admin.register(District)
class DistrictAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'state', location)
    list_filter = ('state',)
    search_fields = ('name',)
    autocomplete_fields = ('state',)
    default_lon, default_lat = WGS84_to_Google(20.5937, 78.9629)

@admin.register(DistrictEditor)
class DistrictEditorAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user', 'district')

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    search_fields = ('service_type',)
    pass

@admin.register(Service)
class ServiceAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'service_type', 'district', location)
    list_filter = ('service_type', 'district__state', 'district')
    autocomplete_fields = ('district', 'service_type')
    default_lon, default_lat = WGS84_to_Google(20.5937, 78.9629)

@admin.register(ServiceChangeRequest)
class ServiceChangeRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'changes', 'approved', 'approved_by')
    list_filter = ('service__service_type', 'service__district__state', 'service__district')