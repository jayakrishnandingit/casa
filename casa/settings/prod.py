import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    '13.234.48.54',
    'ec2-13-234-48-54.ap-south-1.compute.amazonaws.com',
    'jayakrishnandamodaran.com',
    'www.jayakrishnandamodaran.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

CONTACT_EMAIL = "jayakrishnandamodaran@gmail.com"

CHAT_ENABLED = False
RESUME_DOWNLOAD_ALLOWED = False

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
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False
        },
        'casa': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'home': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    },
}
