from headers import Headers
from fluffyurl.url import Url


class Request(object):

    """A Request object."""

    def __init__(self, method, url, headers=Headers(), content=None):
        # XXX no content on GET / DELETE ?
        self.method = method
        self.content = content

        if not isinstance(url, Url):
            url = Url(url)
        self.url = url

        if not isinstance(headers, Headers):
            headers = Headers(headers)
        self._headers = headers

        methods_from_headers = ['if_modified_since', 'if_unmodified_since']
        for m in methods_from_headers:
            setattr(self.__class__, m, getattr(headers, m))

    def _get_method(self):
        return self._method

    def _set_method(self, value):
        self._method = str(value)

    def header(self, name, value=None):
        if value is None:
            return self._headers.get(name)
        else:
            self._headers[name] = value

    @property
    def headers(self):
        return self._headers

    method = property(_get_method, _set_method)
