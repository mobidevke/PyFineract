Introduction
============

PyFineract is Python (2 and 3) library to access an
`Apache Fineract Api <https://demo.openmf.org/api-docs/apiLive.htm#top>`__. This library enables you to manage resources
such as clients, loans, loan products etc in your python applications.


Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with PyFineract,
please `open an issue <https://github.com/mobidevke/PyFineract/issues>`__.

Tutorial (Short)
----------------

First create a Fineract instance::

    from fineract import Fineract

    # First create a Fineract instance

    # using username, password, tenant and base url
    f = Fineract("mifos", "password", "default, "https://localhost/fineract-provider/api/v1")

Then work with your Fineract objects::

    for client in f.get_clients():
        print(client.full_name)


Download and install
--------------------

This package is in the `Python Package Index
<http://pypi.python.org/pypi/PyFineract>`__, so ``pip install PyFineract`` should
be enough.  You can also clone it on `Github
<http://github.com/mobidevke/PyFineract>`__.


Licensing
---------

PyFineract is distributed under the Apache Foundation License.
