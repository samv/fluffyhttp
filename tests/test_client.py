from unittest2 import TestCase
from fluffyhttp.client import Client
from fluffyhttp.request import Request
from fluffyhttp.response import Response


tests = {
    'GET': {
        'url': 'http://lumberjaph.net',
        'headers': {'Accept-Type': 'text/html'}
    },
    'POST': {
        'url': 'http://lumberjaph.net',
        'headers': {'Content-Type': 'text/plain'},
        'content': 'foo',
    }
}

def _test_cb(request):
    if isinstance(request, Request) is False:
        print "not a Request object"
        raise Exception

    if request.method is False:
        print "no HTTP method"
        raise Exception

    method = request.method

    if str(request.url) != tests[method]['url']:
        print "%s is different from %s" % (request.url, tests[method]['url'])
        raise Exception

    if method in ['PUT', 'POST']:
        if request.content != tests[method]['content']:
            print "%s is different from %s" % (request.content, tests[method]['content'])
            raise Exception

    return Response(status=204)

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

    def test_requests(self):
        for method in ['GET', 'POST']:
            self._test_request(method)

    def _test_request(self, method):
        client = Client()
        client.add_handler('request_send', _test_cb)

        request = Request(method, tests[method]['url'], tests[method]['headers'])

        if 'content' in tests[method]:
            request.content = tests[method]['content']

        resp = client.request(request)

        self.assertTrue(resp)
        self.assertEqual(resp.status, 204)
