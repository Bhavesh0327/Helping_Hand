from django.db import models
import django.utils.timezone as tz
from django.contrib.gis.db.models import PointField
from django.forms.models import model_to_dict


class AutoCreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True, editable=False)

    objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = tz.now()
            self.updated_at = self.created_at
        else:
            auto_updated_at_is_disabled = kwargs.pop("disable_auto_updated_at", False)
            if not auto_updated_at_is_disabled:
                self.updated_at = tz.now()
        super(AutoCreatedUpdatedMixin, self).save(*args, **kwargs)

class LocationMixin(models.Model):
    location = PointField()

    class Meta:
        abstract = True

    @property
    def latitude(self):
        return self.location.y

    @property
    def longitude(self):
        return self.location.x

    def to_dict(self):
        d = model_to_dict(self)
        del d['location']
        d['latitude'] = self.latitude
        d['longitude'] = self.longitude
        return d