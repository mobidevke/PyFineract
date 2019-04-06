import requests


def server_test():
    res = requests.get('https://127.0.0.1:8443/api-docs/apiLive.htm', verify=False)
    return res.ok


collect_ignore = []
if not server_test():
    collect_ignore_glob = ['integration/*.py']