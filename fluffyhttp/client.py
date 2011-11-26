from request import Request
from response import Response
from headers import Headers
from exception import *
from url import Url
from urllib3.poolmanager import PoolManager
from urllib3 import connectionpool, poolmanager


class Client(object):

    def __init__(self, agent=None, timeout=10, keep_alive=1,
            default_headers={}, max_redirect=7):

        self.timeout = 60
        self.max_redirect = max_redirect

        if agent is None:
            self.agent = 'python-fluffyhttp'
        else:
            self.agent = agent

        if len(default_headers) == 0:
            default_headers = {
                'Connection': 'keep-alive',
            }

        if 'User-Agent' not in default_headers:
            default_headers['User-Agent'] = self.agent

        self._default_headers = Headers(default_headers)

        self._poolmanager = PoolManager(
            maxsize=keep_alive
        )

    def default_header(self, key):
        return self.default_headers.get('key')

    @property
    def default_headers(self):
        return self._default_headers

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
                self.default_headers.items() + headers.items())
        return final_headers
