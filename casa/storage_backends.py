from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class CasaS3StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION


class CasaS3MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
