from unittest2 import TestCase
from fluffyhttp.handlers import Handlers
from fluffyhttp.request import Request
from fluffyhttp.response import Response


def _cb_request_send(request):
    return Response(status=204)


class TestHandlers(TestCase):

    def test_simple_handler(self):
        handlers = Handlers()
        self.assertTrue(handlers)

    def test_add_handler(self):
        handlers = Handlers()
        handlers.append('request_send', _cb_request_send)
        self.assertEqual(len(handlers.handlers('request_send')), 1)

    def test_execute_handler(self):
        request = Request('GET', 'http')
        handlers = Handlers()
        handlers.append('request_send', _cb_request_send)
        resp = handlers.dispatch('request_send', request)
        self.assertIsInstance(resp, Response)
