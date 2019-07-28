from django.conf import settings


def contact_details(request):
    return {
        'CONTACT_EMAIL': settings.CONTACT_EMAIL
    }


def secrets(request):
    return {
        'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY
    }