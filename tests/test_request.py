from unittest2 import TestCase
from fluffyhttp.request import Request


class TestClient(TestCase):

    def test_base(self):
        request = Request('GET', 'http://github.com')
        self.assertTrue(request)
        self.assertEqual(request.method, 'GET')
