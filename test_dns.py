import os
import unittest

ENV_KEY = 'DREAMHOST_API_KEY'
PUBLIC_DREAMHOST_KEY = '6SHU5P2HLDAYECUM'

# Set the public DreamHost API key before importing the client, since it will
# try to get the value of os.environ[ENV_KEY] immediately.
previous_api_key = os.environ.get(ENV_KEY, None)
os.environ[ENV_KEY] = PUBLIC_DREAMHOST_KEY

import dns

# Once the import is complete, we can put the old key back, if necessary.
if previous_api_key:
    os.environ[ENV_KEY] = previous_api_key


class DNSTest(unittest.TestCase):
    
    def test_list(self):
        self.assertIsNotNone(dns.list())
    
    def test_get(self):
        expected = {
            "zone":       "groo.com",
            "value":      "173.236.152.210",
            "account_id": "1",
            "record":     "groo.com",
            "comment":    "",
            "editable":   "0",
            "type":       "A",
        }
        self.assertEqual(dns.get("groo.com"), expected)
