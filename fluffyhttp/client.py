from request import Request
from response import Response
from headers import Headers
from handlers import Handlers
from exception import *
from url import Url
from urllib3.poolmanager import PoolManager
from urllib3 import connectionpool, poolmanager


class Client(object):

    def __init__(self, agent=None, timeout=10, keep_alive=1,
            default_headers={}, max_redirect=7):

        self.timeout = 60
        self.max_redirect = max_redirect
        self._handlers = Handlers()

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


    def add_handler(self, position, cb):
        self._handlers.append(position, cb)

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
        request = Request('PUT', url, headers=headers, content=content)
        return self._request(request)

    def post(self, url, headers={}, content=None):
        request = Request('PUT', url, headers=headers, content=content)
        return self._request(request)

    def delete(self, url, headers={}, content=None):
        request = Request('DELETE', url, headers=headers)
        return self._request(request)

    def _request(self, request):
        url = request.url
        conn = connectionpool.connection_from_url(str(url))

        headers = self._merge_headers(request.headers)

        try:
            dispatch_response = self._handlers.dispatch('request_send', request)
            if (isinstance(dispatch_response, Response)):
                return dispatch_response
        except Exception, e:
            raise e

        try:
            # XXX fix in Url
            path = '/'.join(request.url.path) or '/'
            r = conn.urlopen(
                method=request.method,
                url=path,
                headers=headers,
                timeout=self.timeout,
                body=request.content,
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
