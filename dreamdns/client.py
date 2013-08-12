"""
Python interface for the DreamHost REST API. Provides a lower-level foundation
for more-specific helper functions to build on.
"""

import datetime
import os

import requests

API_ROOT = 'https://api.dreamhost.com/'
API_KEY  = os.environ['DREAMHOST_API_KEY'] # Do you need to set the env var?

# {url: {when: timestamp, result: response}}
CACHE = {}

def run(command, arguments=None, maxcachetime=0):
    """Executes the given command (with arguments, if any) through the
    DreamHost REST API. Results are returned in JSON. To utilize the cache,
    set maxcachetime greater than zero (this is the number of seconds the
    response for a GET URL request will be cached)."""
    
    parameters = {
        'key': API_KEY,
        'cmd': command,
        'format': 'json',
    }
    
    if arguments:
        parameters.update(arguments)
    
    session = requests.Session()
    prepped = requests.Request('GET', API_ROOT, params=parameters).prepare()
    if maxcachetime > 0:
        url = prepped.url
        try:
            delta = datetime.datetime.now() - CACHE[url]['when']
            if delta.seconds < maxcachetime:
                response = CACHE[url]['result']
            else:
                raise RuntimeError # Cache expired, repopulate!
        except:
            response = session.send(prepped)
            CACHE[url] = {'result': response, 'when': datetime.datetime.now()}
    else:
        response = session.send(prepped)
    
    return response.json()

