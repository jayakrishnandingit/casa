from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActivityTracker(Timestamp):
    """
    Model to track the activities in certain pages in a site.
    """
    activity = models.TextField(null=False, blank=False)
    path = models.URLField(max_length=500, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    from_ip = models.GenericIPAddressField(null=True, blank=True)
    geoip_details = JSONField(null=True, blank=True)
