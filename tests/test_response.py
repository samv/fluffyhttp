from unittest2 import TestCase
from fluffyhttp.response import Response
from fluffyurl.url import Url


class TestClient(TestCase):

    def test_base(self):
        response = Response(status=200, message='OK')
        self.assertTrue(response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.message, 'OK')
        self.assertEqual(response.status_line, '200 OK')

