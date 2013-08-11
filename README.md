dreamdns
========

A python interface to DreamHost's DNS API.

Installing
----------

Install via pip and store your API key in the environment:

```shell
$ pip install -e git+https://github.com/eallrich/dreamdns.git#egg=Package
$ export DREAMHOST_API_KEY="PUT_API_KEY_HERE"
```

Using the library
-----------------

```python
>>> import dreamdns
>>> r = dreamdns.list()
>>> print r['data']
```

Running the tests
-----------------

DreamHost kindly provides a read-only API key for testing. This key is used
for these tests, but it means that only read-only functions are tested.

```shell
$ python -m unittest test_dns
```
