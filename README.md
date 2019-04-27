# PyFineract

[![PyPI](https://img.shields.io/pypi/v/PyFineract.svg)](https://pypi.python.org/pypi/PyFineract)
[![Build Status](https://travis-ci.org/mobidevke/PyFineract.svg?branch=master)](https://travis-ci.org/mobidevke/PyFineract)
[![Coverage Status](https://coveralls.io/repos/github/mobidevke/PyFineract/badge.svg?branch=master)](https://coveralls.io/github/mobidevke/PyFineract?branch=master)

PyFineract is a Python (2 and 3) library to access an 
[Apache Fineract Api](https://demo.openmf.org/api-docs/apiLive.htm#top). This library enables you to manage resources 
such as clients, loans, loan products etc in your python applications.


### Install

```
$ pip install PyFineract
```

### Demo

```
from fineract import Fineract

# First create a Fineract instance

# using username, password, tenant and base url
f = Fineract("mifos", "password", "default, "https://localhost/fineract-provider/api/v1")

# Then play with Fineract objects:
for client in f.get_clients():
    print(client.full_name)
    
```

### Raw Requests
Since this project is still in it's early stages of development, we have provided a method that can be used 
to make raw requests.
```
clients = f.raw_request('GET', '/clients', params={'limit': 10})
print(clients)
```
### Documentation (WIP)
Full documentation can be found [here](https://pyfineract.readthedocs.io).
