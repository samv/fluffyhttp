from unittest2 import TestCase
from fluffyhttp.client import Client


class TestClient(TestCase):

    def test_base(self):
        client = Client()
        self.assertTrue(client)
        self.assertEqual(client.agent, 'python-fluffyhttp')
        client = Client(agent='foo')
        self.assertEqual(client.agent, 'foo')

    def test_headers(self):
        client = Client()
        self.assertTrue(client.default_headers.get('Connection'))
        self.assertEqual(client.default_headers.get('User-Agent'), 'python-fluffyhttp')
