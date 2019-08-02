from django.conf import settings


def contact_details(request):
    return {
        'CONTACT_EMAIL': settings.CONTACT_EMAIL
    }


def secrets(request):
    return {
        'CAPTCHA_PUBLIC_KEY': settings.CAPTCHA_PUBLIC_KEY
    }