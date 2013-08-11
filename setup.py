try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='dreamdns',
    version='0.1',
    packages=['dreamdns',],
    install_requires=['requests == 1.2.3',],
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
)
