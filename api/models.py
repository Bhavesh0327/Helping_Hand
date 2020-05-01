from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.base_user import AbstractBaseUser
from .managers.user_manager import UserManager
from .model_mixins import AutoCreatedUpdatedMixin, LocationMixin


# Create your models here.

class State(AutoCreatedUpdatedMixin, LocationMixin):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class District(AutoCreatedUpdatedMixin, LocationMixin):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    editors = models.ManyToManyField(User, through='DistrictEditor')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class DistrictEditor(AutoCreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

class ServiceType(AutoCreatedUpdatedMixin):
    service_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['service_type']

    def __str__(self):
        return self.service_type


class Service(AutoCreatedUpdatedMixin, LocationMixin):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_active = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name


class ServiceChangeRequest(AutoCreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_change_requests")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="change_requests")
    changes = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_change_request")
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approved_service_change_requests")
