def http_exception(resp):
    raise HTTPException(resp.status, reason=resp.reason, headers=[])

class HTTPException(Exception):

    def __init__(self, status, reason, headers):
        self.status = status
        self.reason = reason
        pass

    def __str__(self):
        return "%i %s" % (self.status, self.reason)

    def is_redirect(self):
        if self.status >= 300 and self.status < 400:
            return True
        return False

    def is_client_error(self):
        if self.status >= 400 and self.status < 500:
            return True
        return False

    def is_server_error(self):
        if self.status >= 500 and self.status < 600:
            return True
        return False
