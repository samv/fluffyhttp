# fluffyhttp (yet another http lib for Python)

## Synopsis

    client = fluffyhttp.Client(useragent='my fluffy client')
    request = fluffyhttp.Request(GET, 'http://github.com')
    response = client.request(request)
    print response.status

### Client

### Request

### Response

### Exceptions

## How to use fluffyhttp

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
