import ssl
from functools import wraps

import requests


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar


ssl.wrap_socket = sslwrap(ssl.wrap_socket)  # see https://stackoverflow.com/a/24166498/3716006


def server_test():
    res = requests.get('https://127.0.0.1:8443/api-docs/apiLive.htm', verify=False)
    return res.ok


collect_ignore = []
if not server_test():
    collect_ignore_glob = ['integration/*.py']