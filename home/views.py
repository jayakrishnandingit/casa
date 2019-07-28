import os
import json
import urllib
import mimetypes

from django.conf import settings
from django.shortcuts import render
from django import http
from django.views import View
from django.views.generic import TemplateView

from .models import FileUpload
from .utils import RedirectorFactory


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


def ResumeDownloadView(View):
    #TODO: Not tested.
    template_name = 'resume_form.html'

    def get(self, request):
        return render(self.template_name)

    def post(self, request):
        if settings.CAPTCHA_PUBLIC_KEY:
            return self.validate_captcha_and_download(request)
        return download(request)

    def validate_captcha_and_download(self, request)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.CAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if not result['success']:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return render(self.template_name)
        return download(request)

    def download(self, request):
        resume = FileUpload.objects.filter(category__name='resume').first()
        if resume is None:
            return http.HttpResponseNotFound('File not found.')
        file_url = resume.uploaded_file.url
        # TODO: not sure if this will work in production where we plan to use AWS S3.
        # TODO: Testing required. Do we need to pass AWS keys as headers?
        file_content = urllib.request.urlopen(file_url).read().decode()
        response = http.HttpResponse(file_content)
        response['Content-Type'] = mimetypes.guess_type(file_url)
        response['Content-Disposition'] = 'attachement; filename=%s' % resume.name
        return response
