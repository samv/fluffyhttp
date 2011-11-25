class Response(object):

    def __init__(self, status, headers, content, reason):
        print headers
        self.status = status
        self._headers = headers
        self._content = content
        self.reason = reason

    @property
    def is_success(self):
        if self.status >= 200 and self.status < 300:
            return True
        return False

    @property
    def content(self):
        pass

    @property
    def header(self):
        pass

    @property
    def headers(self):
        pass
