import sys
sys.path.append('.')

from fluffyhttp import *

client = Client()
response = client.mirror('http://lumberjaph.net', '/tmp/lj.txt')
