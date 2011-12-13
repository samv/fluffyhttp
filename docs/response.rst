.. _response:

Response
========

Synopsis
--------

::

    >>> response = ua.request(request)
    >>> if response.is_success:
    ...     print response.status
    ... else:
    ...     print response.message
    200

Interface
---------

:class:`Response` instances have the following methods:

.. attribute:: Response.status

.. attribute:: Response.headers

.. attribute:: Response.content

.. attribute:: Response.reason

.. attribute:: Response.last_modified

.. attribute:: Response.date

.. attribute:: Response.expires

.. attribute:: Response.content_is_text

.. attribute:: Response.content_is_xml

.. attribute:: Response.content_is_xhtml

.. method:: Response.is_success()

.. method:: Response.is_redirect()

.. method:: Response.header()
