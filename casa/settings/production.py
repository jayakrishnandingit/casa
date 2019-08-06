from base import *


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


CONTACT_EMAIL = "jayakrishnandamodaran@gmail.com"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None  # some issues with original default public-read reported by storages.
AWS_S3_ENCRYPTION = True

# static file.
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# media file.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
