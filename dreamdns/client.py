"""
Python interface for the DreamHost REST API. Provides a lower-level foundation
for more-specific helper functions to build on.
"""

import os

import requests

API_ROOT = 'https://api.dreamhost.com/'
API_KEY  = os.environ['DREAMHOST_API_KEY'] # Do you need to set the env var?

def run(command, arguments=None):
    """Executes the given command (with arguments, if any) through the DreamHost
    REST API. Results are returned in JSON."""
    
    parameters = {
        'key': API_KEY,
        'cmd': command,
        'format': 'json',
    }
    
    if arguments:
        parameters.update(arguments)
    
    response = requests.get(API_ROOT, params=parameters)
    #print "Running %s" % response.request.url
    
    return response.json()

