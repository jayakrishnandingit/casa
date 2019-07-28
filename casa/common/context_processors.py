from django.conf import settings


def contact_details(request):
    return {
        'CONTACT_EMAIL': settings.CONTACT_EMAIL
    }