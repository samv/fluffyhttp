from request import Request
from response import Response
from headers import Headers
from handlers import Handlers
from exception import *
from fluffyurl.url import Url
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
        self._handlers.add_handler(position, cb)

    def remove_handler(self, position):
        self._handler.remove_handler(position)

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

        try:
            resp = self._make_request(request)
        except Exception, e:
            raise e

        if resp.is_success is False:
            if resp.is_redirect and len(resp.redirects) < self.max_redirect:
                try:
                    return self._follow_redirect(resp, request)
                except Exception, e:
                    raise e
            else:
                http_exception(resp)

        return resp

    def _make_request(self, request):

        try:
            request = self._handlers.dispatch('request_prepare', request)
        except Exception, e:
            response = Response(status=400, message='Bad request', request=request)
            return response

        url = request.url
        conn = connectionpool.connection_from_url(str(url))

        headers = self._merge_headers(request.headers)

        try:
            dispatch_response = self._handlers.dispatch(
                    'request_send', request)
            if (isinstance(dispatch_response, Response)):
                return dispatch_response
        except Exception, e:
            raise e

        # XXX fix in Url
        path = str(request.url.path) or '/'
        r = conn.urlopen(
            method=request.method,
            url=path,
            headers=headers,
            timeout=self.timeout,
            body=request.content,
            redirect=False,
        )
        return self._build_response(r, request)

    def _build_response(self, r, request):
        status = r.status
        headers = Headers(r.headers)
        content = r.data

        resp = Response(
            status=status,
            headers=headers,
            content=content,
            message=r.reason,
            request = request
        )

        new_resp = self._handlers.dispatch('response_done', resp)
        if new_resp is not None:
            resp = new_resp

        req = self._handlers.dispatch('response_redirect', resp)

        if req is not None and isinstance(req, Request):
            return self.request(req)

        return resp

    def _merge_headers(self, headers):
        final_headers = Headers(
                self.default_headers.items() + headers.items())
        return final_headers

    def _follow_redirect(self, resp, r):
        redirects = list()
        while (resp.is_redirect and len(redirects) < self.max_redirect):
            location = resp.header('location')
            if location is None:
                break
            redirects.append(resp)
            req = Request(r.method, location)
            resp = self._make_request(req)
            location = resp.header('location')
        resp.redirects = redirects
        return resp
