from headers import Headers


class Request(object):

    def __init__(self, method, url, headers=Headers(), content=None):
        self.method = method
        self.url = url
        self.content = content
        self._headers = headers

    @property
    def header(self, name):
        pass

    @property
    def headers(self):
        return self._headers
