from django.conf import settings
from django.shortcuts import redirect

from activity.utils import track_activity


class BaseRedirectorInterface(object):
    _url = None

    @property
    def url(self):
        pass

    def redirect(self):
        pass

    def get_activity(self):
        pass

    def log_activity(self):
        pass


class Redirector(BaseRedirectorInterface):
    def __init__(self, request=None):
        self.request = request

    @property
    def url(self):
        return self._url

    def redirect(self):
        self.log_activity()
        return redirect(self.url)  # TODO: validate the URL.

    def log_activity(self):
        activity = self.get_activity()
        track_activity(activity, self.request)


class GitHubRedirector(Redirector):
    _url = settings.GITHUB_URL

    def __init__(self, request=None):
        super().__init__(request)

    def get_activity(self):
        return 'github accessed.'


class LinkedInRedirector(Redirector):
    _url = settings.LINKEDIN_URL

    def __init__(self, request=None):
        super().__init__(request)

    def get_activity(self):
        return 'linkedin accessed.'


class MediumRedirector(Redirector):
    _url = settings.MEDIUM_URL

    def __init__(self, request=None):
        super().__init__(request)

    def get_activity(self):
        return 'medium accessed.'


class RedirectorFactory(object):
    redirectors = {
        'github': GitHubRedirector,
        'linkedin': LinkedInRedirector,
        'medium': MediumRedirector
    }

    @classmethod
    def get_class(cls, site_name, default=None):
        return cls.redirectors.get(site_name, default)
