from unittest2 import TestCase
from fluffyhttp.response import Response
from fluffyhttp.request import Request
from fluffyurl.url import Url


class TestClient(TestCase):

    def test_base(self):
        response = Response(status=200, message='OK')
        self.assertTrue(response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.message, 'OK')
        self.assertEqual(response.status_line, '200 OK')

    def test_request(self):
        request = Request('GET', 'http://foobar')
        response = Response(status=200, message='OK', headers={},
                request=request)
    
    def test_base(self):
        response = Response(status=200, message='OK',
                headers={'Content-Base':'http://foo'})
        self.assertEqual(response.base, 'http://foo')
        response = Response(status=200, message='OK',
                headers={'Content-Location':'http://bar'})
        self.assertEqual(response.base, 'http://bar')
        request = Request('GET', 'http://baz')
        response = Response(status=200, message='OK', request=request)
        self.assertEqual(response.base, 'http://baz')

    def test_date(self):
        response = Response(status=200, message='OK',
                headers={'Last-Modified':'Sat, 02 Jul 2011 07:53:00 GMT'})
        self.assertTrue(response.last_modified())
        self.assertEqual(response.last_modified(), 1309618380)

    def test_content(self):
        response = Response(status=200, message='OK',
                headers={'Content-Type':'text/plain'})
        self.assertTrue(response.content_is_text)
