import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = []

BASE_URL = 'http://' + ALLOWED_HOSTS[0]

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

CONTACT_EMAIL = "jayakrishnandamodaran@gmail.com"

CHAT_ENABLED = False

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
        },
        'home': {
            'handlers': ['console', 'info_file_handler', 'error_file_handler'],
            'level': 'INFO',
            'propagate': False
        }
    },
}
