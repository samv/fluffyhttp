.. _getting_started:

Getting started: How to use fluffyhttp
======================================

fluffyhttp is heavily inspired by LWP. It uses the following concept:

#. a Client object.
#. a Request object.
#. a Response object.

Creating your first client
--------------------------

The client implement a web user agent. It is used to dispatch web requests.

In the most common usage, the application creates a Client, and set the default values for the agent string, the timeout, etc. Then a Request object is created. The request is then passed to the client, which dispatch the request and a Response object is returned.

    >>> from fluffyhttp import *
    >>> client = Client()

The default client will set the timeout to 60 seconds, the useragent string to 'python-fluffyhttp', and the number of redirection to follow to 7.

    >>> client = Client(agent='my uber application', timeout=10)

Creating your first request
---------------------------

    >>> from fluffyhttp import *
    >>> request = Request('GET', 'http://google.com')
    >>> response = client.request(request)

The Response object
-------------------

    >>> response = client.request(request)
    >>> print response.status


Why the name ?
--------------

Let's be honest, is this worst than ``httplib2`` or ``urllib2``, ``urllib3`` and even ``requests`` ?
