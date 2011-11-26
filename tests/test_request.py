from unittest2 import TestCase
from fluffyhttp.request import Request
from fluffyhttp.headers import Headers
from fluffyhttp.url import Url


class TestClient(TestCase):

    def test_base(self):
        request = Request('GET', 'http://github.com')
        self.assertTrue(request)
        self.assertEqual(request.method, 'GET')

    def test_method(self):
        for method in ['GET', 'get', 'gEt']:
            request = Request(method, 'http')
            self.assertEqual(request.method, 'GET')

        request = Request('GET', 'http')
        request.method = 'POST'
        self.assertEqual(request.method, 'POST')
        request.method = 'post'
        self.assertEqual(request.method, 'POST')

    def test_headers(self):
        request = Request('GET', 'http', {'Connection':'keep-alive'})
        self.assertIsInstance(request.headers, Headers)

        headers = Headers({'Connection':'keep-alive'})
        request = Request('GET', 'http', headers)
        self.assertTrue(request)

        self.assertEqual(request.header('connection'), 'keep-alive')

    def test_url(self):
        request = Request('GET', 'http')
        self.assertIsInstance(request.url, Url)


    def test_content(self):
        request = Request('GET', 'http', content='foo')
        self.assertEqual(request.content, 'foo')
