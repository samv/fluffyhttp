.. topic:: Easy-to-use and general-purpose HTTP library in Python

    ``fluffyhttp`` is a http library for Python.

Basic Usage
===========

This module is heavily inspired by LWP.

::

    >>> req = Request('GET', 'http://google.com')
    >>> ua = Client()
    >>> resp = ua.request(req)
    >>> print resp.status

User Guide
==========

.. toctree::
   :maxdepth: 2

   contents
