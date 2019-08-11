import os
import logging
import mimetypes
import requests

from django import http
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .models import FileUpload
from .utils import RedirectorFactory

LOGGER = logging.getLogger(__name__)


# Create your views here.
class HomePage(TemplateView):
    template_name = 'homepage.html'


class RedirectorView(View):
    def get(self, request, external_site_name):
        sites = {'github', 'linkedin', 'medium'}
        if external_site_name not in sites:
            return http.HttpResponseBadRequest("Bad request.")

        Redirector = RedirectorFactory.get_class(external_site_name)
        if Redirector is None:
            return http.HttpResponseBadRequest("Bad request.")

        return Redirector(request).redirect()


class ResumeDownloadView(View):
    #TODO: Not tested.
    template_name = 'resume_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if settings.CAPTCHA_PUBLIC_KEY:
            return self.validate_captcha_and_download(request)
        return self.download(request)

    def validate_captcha_and_download(self, request):
        if self.validate_captcha(request):
            return self.download(request)
        return render(request, self.template_name)
        
    def validate_captcha(self, request):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.CAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        try:
            LOGGER.info("Validating captcha.")
            response =  requests.post(url, data=values)
        except Exception as e:
            messages.error(request, "We are unable to process the request at the moment.")
            LOGGER.error(e)
            return False
        if response.status_code != 200:
            messages.error(request, "We are unable to process the request at the moment.")
            LOGGER.error(e)
            return False
        result = response.json()
        if not result['success']:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return False
        return True

    def download(self, request):
        resume = FileUpload.objects.filter(category__name='resume').first()
        if resume is None:
            messages.error(request, "File not found. Try again later.")
            return http.HttpResponseNotFound('File not found.')
        file_url = resume.uploaded_file.url
        # TODO: not sure if this will work in production where we plan to use AWS S3.
        # TODO: Testing required. Do we need to pass AWS keys as headers?
        try:
            LOGGER.info("Going to download file from the URL %s.", file_url)
            response = requests.get(file_url)
        except Exception as e:
            messages.error(request, "File cannot be downloaded. Please try after sometime.")
            LOGGER.error(e)
            return http.HttpResponseNotFound('File not found.')
        if response.status_code != 200:
            messages.error(request, "File cannot be downloaded. Please try after sometime.")
            LOGGER.error(e)
            return http.HttpResponseNotFound('File not found.')

        file_content = response.raw.read()
        response = http.HttpResponse(file_content)
        response['Content-Type'] = mimetypes.guess_type(file_url)
        response['Content-Disposition'] = 'attachement; filename=%s' % resume.name
        return response
