from headers import Headers


class Response(object):

    def __init__(self, status, headers=Headers(), content=None, message=None, request=None):
        self.status = status
        self.message = message
        self.redirects = list()
        self._headers = headers
        self._content = content
        self._request = request

    @property
    def is_info(self):
        if self.status >= 100 and self.status < 200:
            return True
        return False

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
    def is_client_error(self):
        if self.status >= 400 and self.status < 500:
            return True
        return False

    @property
    def is_server_error(self):
        return self.is_error()
    
    @property
    def is_error(self):
        if self.status >= 500 and self.status < 600:
            return True
        return False

    @property
    def base(self):
        if self.header('Content-Base'):
            return self.header('Content-Base')
        if self.header('Content-Location'):
            return self.header('Content-Location')
        else:
            return self.request.url

    @property
    def request(self):
        return self._request

    @property
    def content(self):
        return self._content

    def header(self, name):
        return self._headers.get(name)

    @property
    def headers(self):
        return self._headers

    @property
    def status_line(self):
        return "{0} {1}".format(self.status, self.message)
