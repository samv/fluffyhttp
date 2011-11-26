from unittest2 import TestCase
from fluffyhttp import Url
from itertools import product

class Test_Url(TestCase):
    flavours = (
        {   'absolute': ('http://example.com', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('host', lambda u: u.host=='example.com'),
                        ('netloc', lambda u: u.netloc=='example.com'),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),
            'relative': ('', (
                        ('is_absolute', lambda u: not u.is_absolute),
                        ('is_relative', lambda u: u.is_relative),
                        ('host', lambda u: u.host is None),
                        ('netloc', lambda u: u.netloc==''),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),
            'secure':   ('https://example.org', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('is_secure', lambda u: u.is_secure),
                        ('host', lambda u: u.host=='example.org'),
                        ('netloc', lambda u: u.netloc=='example.org'),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: u.is_secure),
                        )),
            'auth_w_pass': ('http://toto:pass@example.org', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('host', lambda u: u.host=='example.org'),
                        ('netloc', lambda u: u.netloc=='toto:pass@example.org'),
                        ('username', lambda u: u.username == 'toto'),
                        ('password', lambda u: u.password == 'pass'),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),

        },
        {   ' root': ('/', (
                    ('path', lambda u: u.path == []),
                    )),
            ' w_path': ('/foo/bar/wib.ble', (
                    ('path', lambda u: u.path == ['foo', 'bar', 'wib.ble']),
                    )),
        },
        {   ' vanilla': ( '', (
                       ('query', lambda u: u.query == []),
                       )),
            ' w_query': ('?a=b&a=c&d=e', (
                       ('query', lambda u: u.query == [('a', 'b'), ('a', 'c'), ('d', 'e')]),
                       )),
        }
    )

    def url_flavours(self):
        allitems = [ x.iteritems() for x in self.flavours ]
        return product(*allitems)

    def test_init(self):
        flavours = self.url_flavours()
        for f in flavours:
            msg = reduce(lambda a, b: a+b[0], f, '')
            urlstr = reduce(lambda a, b: a+b[1][0], f, '')
            tests = reduce(lambda a, b: a+b[1][1], f, tuple())
            url = Url(urlstr)
            for tname, predicate in tests:
                self.assertTrue(predicate(url), msg=msg+": "+tname)
            copy = Url(str(url))
            self.assertEqual(str(copy), str(url), msg="copy is not identical")

    def test_netloc(self):
        u=Url()
        self.assertTrue(u)
        u.username = 'toto'
        u.password = 'pass'
        u.host = 'foob.ar'
        self.assertEqual('toto:pass@foob.ar', u.netloc)
        self.assertEqual(None, u.port)
        u.netloc = 'toto.com'
        self.assertEqual(None, u.username)
        self.assertEqual(None, u.password)
        self.assertEqual('toto.com', u.host)
        self.assertEqual(None, u.port)

    def test_add(self):
        u = Url('https://foob.ar/some/where/some/thing')
        a = Url('http://foob.it/')
        rel = Url('../../rville')
        self.assertEqual(a, u+a)
        self.assertEqual(u, a+u)
        self.assertEqual(Url('https://foob.ar/some/rville'), u+rel)
        self.assertEqual(u, rel+u)


## Url can be defined by a string
#rel = Url('../c')
#rel.path
#rel.host
#rel.is_absolute
#rel.is_relative
#example = Url('http://www.example.com')
#example.host
#example.is_absolute
#example.is_relative
## Url can be defined by named arguments
#u=Url(host='foo.bar', path=('a','b'))
#u
#u.query.append(('arg', 'value'))
#u
#u.query.append(('more tricky', 'full #of:crap'))
#u
#repr(u)
## username,password,host,port and netloc can be interchangeably edited
#u.username = 'toto'
#u.netloc
#u.netloc='bl0b:pouet@example.com'
#u.password
#u.username
#u.host
#u.port
#u.port = 80
#u.netloc
#u
## Url can be appended to another one.
#u+rel
#u+example
#rel+example
