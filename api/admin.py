from django.contrib import admin
from api.models import District, DistrictEditor, State, Service, ServiceChangeRequest, ServiceType
from api.helpers.admin import location

# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', location)
    search_fields = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', location)
    list_filter = ('state',)
    search_fields = ('name',)
    autocomplete_fields = ('state',)

@admin.register(DistrictEditor)
class DistrictEditorAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user', 'district')

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    search_fields = ('service_type',)
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service_type', 'district', location)
    list_filter = ('service_type', 'district__state', 'district')
    autocomplete_fields = ('district', 'service_type')

@admin.register(ServiceChangeRequest)
class ServiceChangeRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'changes', 'approved', 'approved_by')
    list_filter = ('service__service_type', 'service__district__state', 'service__district')