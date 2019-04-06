import ssl
import time
from functools import wraps

import requests

timeout = 75


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar


ssl.wrap_socket = sslwrap(ssl.wrap_socket)  # see https://stackoverflow.com/a/24166498/3716006


def wait_for_fineract():
    seconds = 0
    while seconds < timeout:
        res = requests.get('https://127.0.0.1:8443/api-docs/apiLive.htm', verify=False)
        if res.ok:
            print('Available after {} seconds.'.format(seconds))
            break

        print('Waiting for fineract instance...')
        time.sleep(5)
        seconds += 5


wait_for_fineract()
