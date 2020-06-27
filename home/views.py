import logging
import mimetypes
import requests

from django import http
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models import FileUpload

LOGGER = logging.getLogger(__name__)


# Create your views here.
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

        LOGGER.info(f"Downloading the file {resume.uploaded_file.url}.")
        response = http.HttpResponse(resume.uploaded_file.read())
        # TODO: content type and extension is not parsed correctly.
        file_extension = ""
        content_type, encoding = mimetypes.guess_type(resume.uploaded_file.url)
        if content_type:
            LOGGER.info(f"Content type found is {content_type}.")
            response['Content-Type'] = content_type
            file_extension = mimetypes.guess_extension(content_type)
        filename = f"{resume.name}{file_extension}"
        response['Content-Disposition'] = 'attachement; filename=%s' % filename
        return response
