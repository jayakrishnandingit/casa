from base import *


DEBUG = False

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

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')  # TODO: move to AWS S3.
# append an md5 hash to the static files to bust cache.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

CONTACT_EMAIL = "jayakrishnandamodaran@gmail.com"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None  # some issues with original default public-read reported by storages.
AWS_S3_ENCRYPTION = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
