# fluffyhttp (yet another http lib for Python)

fluffyhttp is heavily inspired by LWP.

## Synopsis

    >>> from fluffyhttp import *
    >>> client = fluffyhttp.Client(useragent='my fluffy client')
    >>> request = fluffyhttp.Request(GET, 'http://pypi.python.org')
    >>> response = client.request(request)
    >>> print response.status
    200

## How to use fluffyhttp

### Doc

http://fluffyhttp.rtfd.org/

### Git

    git clone git://github.com/franckcuny/fluffyhttp.git
    cd fluffyhttp
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-tests.txt
    ./run_tests.py tests/test_*
    python eg/simple.py

## TODO

 * doc
 * docstring
 * moar tests
 * post/put/delete
 * redirect
 * moar exceptions
