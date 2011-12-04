.. _request:

Request
=======

Synopsis
--------

::

    >>> request = Request('GET', 'http://pypi.python.org')

And usually used like this:

    >>> ua = Client()
    >>> response = ua.request(request)

Interface
---------

:class:`Request` instances have the following methods:

.. attribute:: Request.method

.. attribute:: Request.url

.. attribute:: Request.headers

.. attribute:: Request.content

.. method:: Request.header()
