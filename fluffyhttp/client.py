from fluffyhttp.request import Request
from fluffyhttp.response import Response
import httplib2


class Client(object):
    useragent = 'fluffyhttp client'
    timeout = 60

    def __init__(self, useragent=None, timeout=None):

        if useragent is not None:
            self.useragent = useragent

        if timeout is not None:
            self.timeout = timeout

    def request(self, request):
        return self._request(request)

    def get(self, url):
        pass

    def put(self, url):
        pass

    def post(self, url):
        pass

    def delete(self, url):
        pass

    def _request(self, request):
        h = httplib2.Http()
        headers, content = h.request(request.url, request.method)

        status = headers['status']
        del(headers['status'])

        resp = Response(status=200, headers=headers, content=content)
        return resp
