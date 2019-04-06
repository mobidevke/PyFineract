import time

import requests

timeout = 75

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