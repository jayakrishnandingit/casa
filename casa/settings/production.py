import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = []

BASE_URL = 'http://' + ALLOWED_HOSTS[0]

INSTALLED_APPS += [
    'storages'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    }
}

GEOIP_PATH = os.path.join(BASE_DIR, 'geodata', 'GeoLite2-City_20190716', 'GeoLite2-City.mmdb')

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None  # some issues with original default public-read reported by storages.
AWS_S3_ENCRYPTION = True
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# static file.
STATICFILES_STORAGE = 'casa.storage_backends.CasaS3StaticStorage'
AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
# media file.
DEFAULT_FILE_STORAGE = 'casa.storage_backends.CasaS3MediaStorage'
AWS_MEDIA_LOCATION = 'uploads'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'

CONTACT_EMAIL = "jayakrishnandamodaran@gmail.com"

CHAT_ENABLED = False

CAPTCHA_PUBLIC_KEY = None
CAPTCHA_SECRET_KEY = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'info_file_handler': {
            'class': 'logging.RotatingFileHanler',
            'formatter': 'verbose',
            'file': '/var/log/casa_info.log',
            'level': 'INFO'
        },
        'error_file_handler': {
            'class': 'logging.RotatingFileHanler',
            'formatter': 'verbose',
            'file': '/var/log/casa_error.log',
            'level': 'ERROR'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'info_file_handler', 'error_file_handler'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False
        },
        'casa': {
            'handlers': ['console', 'info_file_handler', 'error_file_handler'],
            'level': 'INFO',
            'propagate': False
        }
    },
}
