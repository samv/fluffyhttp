from unittest2 import TestCase
from fluffyhttp.client import Client


class TestClient(TestCase):

    def test_base(self):
        client = Client()
        self.assertTrue(client)
        self.assertEqual(client.useragent, 'python-fluffyhttp')
        client = Client(useragent='foo')
        self.assertEqual(client.useragent, 'foo')
