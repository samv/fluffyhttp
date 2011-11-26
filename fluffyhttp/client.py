from request import Request
from response import Response
from headers import Headers
from exception import *
from url import Url
from urllib3.poolmanager import PoolManager
from urllib3 import connectionpool, poolmanager


class Client(object):

    def __init__(self, useragent=None, timeout=10, keep_alive=1, headers=None,
            max_redirects=7):

        self.timeout = 60
        self.max_redirects = max_redirects

        if useragent is None:
            self.useragent = 'python-fluffyhttp'
        else:
            self.useragent = useragent

        if headers is None:
            headers = {
                'Connection': 'keep-alive',
            }

        if 'User-Agent' not in headers:
            headers['User-Agent'] = self.useragent

        self._default_headers = Headers(headers)

        self._poolmanager = PoolManager(
            maxsize=keep_alive
        )

    def request(self, request):
        return self._request(request)

    def head(self, url, headers={}):
        request = Request('HEAD', url, headers=headers)
        return self._request(request)

    def get(self, url, headers={}):
        request = Request('GET', url, headers=headers)
        return self._request(request)

    def put(self, url, headers={}, content=None):
        pass

    def post(self, url, headers={}, content=None):
        pass

    def delete(self, url, headers={}, content=None):
        pass

    def _request(self, request):
        url = str(request.url)
        conn = connectionpool.connection_from_url(url)

        headers = self._merge_headers(request.headers)

        try:
            r = conn.urlopen(
                method=request.method,
                url=url,
                headers=headers,
                timeout=self.timeout
            )
            return self._build_response(r)
        except Exception, e:
            raise e

    def _build_response(self, r):
        status = r.status
        headers = Headers(r.headers)
        content = r.data

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
        final_headers = Headers(
                self._default_headers.items() + headers.items())
        return final_headers
