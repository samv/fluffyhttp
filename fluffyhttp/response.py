from headers import Headers


class Response(object):

    def __init__(self, status, headers=Headers(), content=None, reason=None):
        self.status = status
        self._headers = headers
        self._content = content
        self.reason = reason
        self.redirects = list()

    @property
    def is_success(self):
        if self.status >= 200 and self.status < 300:
            return True
        return False

    @property
    def is_redirect(self):
        if self.status >= 300 and self.status < 400:
            return True
        return False

    @property
    def content(self):
        return self._content

    def header(self, name):
        return self._headers.get(name)

    @property
    def headers(self):
        pass
