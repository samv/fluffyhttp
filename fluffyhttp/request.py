from headers import Headers
from url import Url


class Request(object):

    def __init__(self, method, url, headers=Headers(), content=None):
        self.method = method
        self.content = content

        if not isinstance(url, Url):
            url = Url(url)
        self.url = url

        if not isinstance(headers, Headers):
            headers = Headers(headers)
        self._headers = headers

    @property
    def header(self, name):
        pass

    @property
    def headers(self):
        return self._headers
