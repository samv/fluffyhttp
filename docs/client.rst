.. _client:

Client
======

Synopsis
--------

::

    >>> client = Client()
    >>> client.timeout = 10
    >>> resp = client.get('http://pypi.python.org/')
    >>> print resp.status

Handlers
--------

Handlers are code that injected at various phases during the processing of requests.

::

    >>> client = Client()
    >>> client.add_handler('request_prepare', before_request)

Interface
---------

:class:`Client` instances have the following methods:

.. attribute:: Client.timeout

    Value of the timeout. Default is set to 60 seconds.

.. attribute:: Client.max_redirect

    Number of redirections the client will follow. Default is set to 7.

.. attribute:: Client.agent

    User-agent string the client will use to identify itself. Default set to `python-fluffyhttp`.

.. attribute:: Client.default_headers

    Dictionary of default headers to send with each request. Default is `Connection: keep-alive`.

.. method:: Client.request(request)

    Dispatch the request and return a ``Response`` object.

.. method:: Client.head(url[, headers])

    Dispatch a ``head`` request and return a ``Response`` object.

.. method:: Client.get(url[, headers])

    Dispatch a ``get`` request and return a ``Response`` object.

.. method:: Client.put(url[, headers, content])

    Dispatch a ``put`` request and return a ``Response`` object.

.. method:: Client.post(url[, headers, content])

    Dispatch a ``post`` request and return a ``Response`` object.

.. method:: Client.delete(url[, headers, content])

    Dispatch a ``delete`` request and return a ``Response`` object.

.. method:: Client.default_header(key)

.. method:: Client.add_handler(position, call_back)

.. method:: Client.remove_handler(position)
