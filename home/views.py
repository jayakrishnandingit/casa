from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.views import View
from django.views.generic import TemplateView

from .utils import RedirectorFactory


# Create your views here.
class HomePage(TemplateView):
    template_name = 'homepage.html'


class RedirectorView(View):
    def get(self, request, external_site_name):
        sites = {'github', 'linkedin', 'medium'}
        if external_site_name not in sites:
            return HttpResponseBadRequest("Bad request.")

        Redirector = RedirectorFactory.get_class(external_site_name)
        if Redirector is None:
            return HttpResponseBadRequest("Bad request.")

        return Redirector(request).redirect()
