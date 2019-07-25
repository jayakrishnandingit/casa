from base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')  # TODO: move to AWS S3.
# append an md5 hash to the static files to bust cache.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
