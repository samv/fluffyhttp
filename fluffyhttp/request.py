from headers import Headers
from url import Url


class Request(object):

    """A Request object."""

    def __init__(self, method, url, headers=Headers(), content=None):
        self.method = method
        self.content = content

        if not isinstance(url, Url):
            url = Url(url)
        self.url = url

        if not isinstance(headers, Headers):
            headers = Headers(headers)
        self._headers = headers

    def _get_method(self):
        return self._method

    def _set_method(self, value):
        self._method = str(value).upper()

    def header(self, name):
        return self._headers.get(name)

    @property
    def headers(self):
        return self._headers

    method = property(_get_method, _set_method)
