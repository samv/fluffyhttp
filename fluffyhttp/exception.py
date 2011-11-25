def http_exception(status):
    raise HTTPException(status, reason='foo', headers=[])

class HTTPException(Exception):

    def __init__(self, status, reason, headers):
        self.status = status
        pass

    def __str__(self):
        pass

    def is_redirect(self):
        if self.status >= 300 and self.status < 400:
            return True
        return False
