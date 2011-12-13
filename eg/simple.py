import sys
sys.path.append('.')

from fluffyhttp import *

client = Client()
request = Request('GET', 'http://lumberjaph.net')
response = client.request(request)

if response.is_success:
    print "yeah, success!"
    print "status: {status}".format(status=response.status)
    print "message: {message}".format(message=response.message)
    print "last modified in epoch: {last_modified}".format(last_modified=response.last_modified())
    print "last modified in string: {last_modified}".format(last_modified=response.header('Last-Modified'))
    if response.content_is_text:
        print "and our content is text!"
else:
    print "oups! {status_line}".format(status_line=response.status_line)
