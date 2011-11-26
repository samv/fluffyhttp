from unittest2 import TestCase
from fluffyhttp.headers import Headers


class TestHeaders(TestCase):

    def test_simple(self):
        headers = {
            'Content-Type': 'application/json'
        }

        f_headers = Headers(headers)
        self.assertTrue(f_headers)

        self.assertTrue(f_headers.get('Content-Type'))
        self.assertTrue(f_headers.get('content-type'))

        f_headers['User-Agent'] = 'fluffy'
        self.assertTrue(f_headers.get('User-Agent'))
        self.assertTrue(f_headers.get('user-agent'))

