from unittest2 import TestCase
from fluffyhttp.client import Client
from fluffyhttp.handlers import Handlers
from fluffyhttp.request import Request
from fluffyhttp.response import Response


def _cb_request_prepare(request):
    raise

def _cb_request_prepare_change_request(request):
    request = Request('PUT', 'http')
    return request

def _cb_request_prepare_do_nothing(request): pass

def _cb_request_send(request):
    return Response(status=204)

def _cb_response_done(response):
    return Response(status=202)

class TestHandlers(TestCase):

    def test_simple_handler(self):
        handlers = Handlers()
        self.assertTrue(handlers)

    def test_add_remove_handler(self):
        handlers = Handlers()
        handlers.add_handler('request_send', _cb_request_send)
        self.assertTrue(handlers.handlers('request_send'))

        handlers.remove_handler('request_send')
        self.assertFalse(handlers.handlers('request_send'))

    def test_execute_handler(self):
        request = Request('GET', 'http')
        handlers = Handlers()
        handlers.add_handler('request_send', _cb_request_send)
        resp = handlers.dispatch('request_send', request)
        self.assertIsInstance(resp, Response)

    def test_overwrite_handlers(self):
        request = Request('GET', 'http')
        handlers = Handlers()
        handlers.add_handler('request_send', lambda r: 1)
        resp = handlers.dispatch('request_send', request)
        self.assertEqual(resp, 1)

        handlers.add_handler('request_send', lambda r: 2)
        resp = handlers.dispatch('request_send', request)
        self.assertEqual(resp, 2)

    def test_prepare(self):
        request = Request('FOO', 'http')
        client = Client()
        client.add_handler('request_prepare', _cb_request_prepare)

        resp = client.request(request)
        self.assertEqual(resp.status, 400)

        handlers = Handlers()
        handlers.add_handler('request_prepare', _cb_request_prepare_change_request)
        req = handlers.dispatch('request_prepare', request)
        self.assertEqual(req.method, 'PUT')

        handlers = Handlers()
        handlers.add_handler('request_prepare', _cb_request_prepare_do_nothing)
        req = handlers.dispatch('request_prepare', request)
        self.assertEqual(req.method, 'FOO')
        self.assertEqual(req.url, 'http')

    def test_response(self):
        request = Request('GET', 'http')
        client = Client()
        client.add_handler('request_send', _cb_request_send)
        #client.add_handler('response_done', _cb_response_done)
        resp = client.request(request)
        #self.assertTrue(resp.status, 202)

    def test_redirect(self):
        pass

    def test_unexisting_phase(self):
        handler = Handlers()
        with self.assertRaises(Exception) as cm:
            handler.handlers('foo')
        exception = cm.exception
        self.assertTrue(exception)
        pass
