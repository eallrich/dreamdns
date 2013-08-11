"""
Python interface for the DreamHost DNS REST API.
"""

import client # Lower-level DreamHost interface


def failed(response):
    """DreamHost does not use HTTP status codes to indicate success or failure,
    relying instead on a 'result' key in the response."""
    try:
        if response['result'] == u'success':
            return False
    except:
        pass
    return True


def list():
    """Returns a list of all DNS records for all domains to which the API key
    has access.""" 
    command = 'dns-list_records'
    
    response = client.run(command)
    
    if failed(response):
        return None
    
    return response['data']


def get(record_name):
    """Retrieves the DNS record (if one exists) for the given record name."""
    # This is a meta-command which simply filters through all the records
    records = list()
    
    if records:
        for r in records:
            if r['record'] == record_name:
                return r
    
    # "Could not retrieve record for '%s'" % record_name
    return None


def add(name, type, value, comment=u''):
    """Adds a DNS record with the given values."""
    command = 'dns-add_record'
    
    arguments = {
        'record':  name,
        'type':    type,
        'value':   value,
        'comment': comment,
    }
    
    response = client.run(command, arguments)
    
    if failed(response):
        reason = response['data']
        message = "Could not add record for '%s': %s" % (name, reason)
        raise RuntimeError(message)


def delete(name, type, value):
    """Deletes the DNS record (if any) which matches the given values."""
    command = 'dns-remove_record'
    
    arguments = {
        'record': name,
        'type':   type,
        'value':  value,
    }
    
    response = client.run(command, arguments)
    
    if failed(response):
        reason = response['data']
        message = "Could not remove record for '%s': %s" % (name, reason)
        raise RuntimeError(message)


def update(name, type, value, comment=u''):
    """Updates the named record with the new values."""
    existing = get(name)
    if existing:
        delete(existing['record'], existing['type'], existing['value'])
    
    add(name, type, value, comment)

