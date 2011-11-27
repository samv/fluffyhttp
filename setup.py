from setuptools import setup
from os.path import join, dirname

try:
    long_description = open(join(dirname(__file__), 'README.rst')).read()
except Exception:
    long_description = None

setup(
    name='fluffyhttp',
    version='0.0.1',
    description='HTTP library',
    author='Franck Cuny',
    author_email='franck.cuny@gmail.com',

    long_description=long_description,
)