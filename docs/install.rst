=======================
Installing `fluffyhttp`
=======================

.. _install_from_github:

Installing from GitHub
======================

At the moment, the only way to get ``fluffyhttp`` is from `GitHub <https://github.com/franckcuny/fluffyhttp>`_.

I also recommend to use `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ and `pip <http://pypi.python.org/pypi/pip>`_ to work wit
h this repository.

To get the sources and install all the requirements::

    git clone git://github.com/franckcuny/fluffyhttp.git
    cd fluffyhttp
    virtualenv env
    source virtualenv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-test.txt

.. _testing:

Testing
=======

First you need to install all the requirements for the tests, following the previous instruction. Then, you can easily run the tests wi
th the following command::

    ./run_tests.py

