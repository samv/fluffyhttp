class Response(object):

    def __init__(self, status, headers, content):
        self.status = status
        self.headers = headers
        self.content = content

    def is_success(self):
        if self.status >= 200 and self.status <300:
            return True
        return False
