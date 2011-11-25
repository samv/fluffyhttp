from unittest2 import TestCase
from fluffyhttp.client import Client


class TestClient(TestCase):

    def test_base(self):
        client = Client()
        self.assertTrue(client)
        self.assertEqual(client.useragent, 'python-fluffyhttp')
        client = Client(useragent='foo')
        self.assertEqual(client.useragent, 'foo')

    def test_headers(self):
        client = Client()
        self.assertTrue(client._default_headers['Connection'])
        self.assertEqual(client._default_headers['User-Agent'], 'python-fluffyhttp')
