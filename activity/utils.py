import logging

from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2

from .models import ActivityTracker

LOGGER = logging.getLogger(__name__)


def track_activity(activity, request=None):
    LOGGER.info('Logging activity %s.', activity)
    request_info = {}
    if request is not None:
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        LOGGER.info('Client IP Address %s.', client_ip)
        geo_details = None
        if client_ip and not settings.DEBUG:
            # find GEO details.
            gp = GeoIP2()
            geo_details = gp.city(client_ip)
            LOGGER.info("GEO details %s.", geo_details)
        request_info = {
            'path': request.META.get('HTTP_REFERER'),
            'from_ip': client_ip,
            'user_agent': request.headers.get('user-agent'),
            'geoip_details': geo_details
        }
    LOGGER.info('Request info gathered is %s.', request_info)
    activity_log = ActivityTracker.objects.create(
        activity=activity,
        **request_info
    )
    return activity_log
