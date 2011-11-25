import sys
sys.path.append('.')

from fluffyhttp.client import Client
from fluffyhttp.request import Request
from fluffyhttp.response import Response


client = Client()
request = Request('GET', 'http://saymedia.com')
response = client.request(request)

if response.is_success():
    print response.headers
else:
    print response.status
