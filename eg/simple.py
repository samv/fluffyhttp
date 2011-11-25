import sys
sys.path.append('.')

from fluffyhttp import *

client = Client()
request = Request('GET', 'http://lumberjaph.net')
response = client.request(request)

if response.is_success:
    print response.status
else:
    print response

try:
    response = client.get('http://lumberjaph.net/foo/bar/baz')
except HTTPException, e:
    if e.is_redirect:
        print "on a une redirection"
    elif e.is_client_error:
        print e
    else:
        print "something else is going on"
