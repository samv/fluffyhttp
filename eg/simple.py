import sys
sys.path.append('.')

from datetime import datetime
from fluffyhttp import *

client = Client(agent='my uber agent')
request = Request('GET', 'http://lumberjaph.net')
request.if_modified_since(datetime(2011, 12, 1, 0, 0))
response = client.request(request)

if response.is_success:
    print "yeah, success!"
    print "status: {status}".format(status=response.status)
    print "message: {message}".format(message=response.message)
    print "content length: {length}".format(length=response.content_length())
    print "last modified in epoch: {last_modified}".format(last_modified=response.last_modified())
    print "last modified in string: {last_modified}".format(last_modified=response.header('Last-Modified'))
    if response.content_is_text:
        #print response.content
        pass
else:
    print "oups! {status_line}".format(status_line=response.status_line)
