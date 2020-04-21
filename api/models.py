from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers.user_manager import UserManager

# Create your models here.

class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    zone = models.CharField(max_length=255)

class ServiceType(models.Model):
    service_type_id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=100)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    district_id = models.ForeignKey(District, db_column='district_id', on_delete=models.CASCADE)
    service_type_id = models.ForeignKey(ServiceType, db_column='service_type_id', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    open_time = models.TimeField()
    close_time = models.TimeField()

class Editor(AbstractBaseUser, PermissionsMixin):
    editor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    editor_id = models.ForeignKey(Editor, db_column='editor_id', on_delete=models.CASCADE)
    request_time = models.TimeField()
    
class RequestApproved(models.Model):
    request_approval_id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(Request, db_column='request_id', on_delete=models.CASCADE)
    approved_by = models.ForeignKey(Editor, db_column='editor_id', on_delete=models.CASCADE)

class RequestChange(models.Model):
    change_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey(Service, db_column='service_id', on_delete=models.CASCADE)
    request_id = models.ForeignKey(Request, db_column='request_id', on_delete=models.CASCADE)
     