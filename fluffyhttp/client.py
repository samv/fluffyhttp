from request import Request
from response import Response
from exception import *
from urllib3.poolmanager import PoolManager
from urllib3 import connectionpool, poolmanager


class Client(object):

    def __init__(self, useragent=None, timeout=None, keep_alive=1, headers=None):

        if useragent is None:
            self.useragent = 'python-fluffyhttp'
        else:
            self.useragent = useragent

        if timeout is None:
            self.timeout = 60
        else:
            self.timeout = timeout

        if headers is None:
            headers = {
                'Connection': 'keep-alive',
            }

        if 'User-Agent' not in headers:
            headers['User-Agent'] = self.useragent

        self._default_headers = headers

        self._poolmanager = PoolManager(
            maxsize=keep_alive
        )

    def request(self, request):
        return self._request(request)

    def get(self, url, headers=dict):
        request = Request('GET', url)
        return self._request(request)

    def put(self, url):
        pass

    def post(self, url):
        pass

    def delete(self, url):
        pass

    def _request(self, request):
        conn = connectionpool.connection_from_url(request.url)

        headers = self._merge_headers(request.headers)

        try:
            r = conn.urlopen(
                method=request.method,
                url=request.url,
                headers=headers)
        except Exception, e:
            print "meh"

        return self._build_response(r)

    def _build_response(self, r):
        status = r.status
        headers = r.headers
        content = 'foo'

        resp = Response(
            status=status,
            headers=headers,
            content=content,
            reason=r.reason,
        )

        if resp.is_success is False:
            http_exception(resp)

        return resp

    def _merge_headers(self, headers):
        final_headers = dict(self._default_headers.items() + headers.items())
        return final_headers
