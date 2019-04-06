# fineract APIs run on https by default
from fineract.handlers import RequestHandler
from fineract.objects.client import Client
from fineract.objects.loan import Loan
from fineract.objects.loan_product import LoanProduct
from fineract.objects.org import Staff, Fund, Charge, Office
from fineract.objects.role import Role
from fineract.pagination import PaginatedList

DEFAULT_BASE_URL = 'https://localhost/fineract-provider/api/v1'
DEFAULT_TENANT = 'default'
DEFAULT_TIMEOUT = 15
DEFAULT_PER_PAGE = 30


class Fineract(object):

    def __init__(self, username=None, password=None, tenant=DEFAULT_TENANT, base_url=DEFAULT_BASE_URL,
                 timeout=DEFAULT_TIMEOUT, per_page=DEFAULT_PER_PAGE, debug=False, ssl_check=True):
        """
        :param username: string
        :param password: string
        :param tenant:  string
        :param base_url: string
        :param timeout: int
        """
        assert username is None or isinstance(username, str), username
        assert password is None or isinstance(password, str), password
        assert tenant is None or isinstance(tenant, str), tenant
        assert base_url is None or isinstance(base_url, str), base_url
        self.__request_handler = RequestHandler(username, password, base_url, tenant, timeout, per_page, debug,
                                                ssl_check)

    @property
    def request_handler(self):
        return self.__request_handler

    def get_roles(self):
        """
        :calls `GET /roles <https://demo.openmf.org/api-docs/apiLive.htm#roles>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.role.Role`
        """
        return PaginatedList(
            Role,
            self.__request_handler,
            '/roles',
            dict()
        )

    def get_clients(self, **kwargs):
        """
        :calls `GET /clients <https://demo.openmf.org/api-docs/apiLive.htm#clients>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.client.Client`
        """
        return PaginatedList(
            Client,
            self.__request_handler,
            '/clients',
            kwargs
        )

    def get_client(self, id):
        """
        :calls `GET /clients/<id> <https://demo.openmf.org/api-docs/apiLive.htm#clients_retrieve>`_
        :rtype: :class:`fineract.objects.client.Client`
        """
        return Client(self.__request_handler,
                      self.__request_handler.make_request(
                          'GET',
                          '/clients/{}'.format(id)
                      ), False)

    def get_loan_products(self, **kwargs):
        """
        :calls `GET /loanproducts <https://demo.openmf.org/api-docs/apiLive.htm#loanproducts>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.loan_product.LoanProduct`
        """
        return PaginatedList(
            LoanProduct,
            self.__request_handler,
            '/loanproducts',
            kwargs
        )

    def get_loan_product(self, id):
        """
        :calls `GET /loanproducts/<id> <https://demo.openmf.org/api-docs/apiLive.htm#loanproducts_retrieve>`_
        :rtype: :class:`fineract.objects.loan_product.LoanProduct`
        """
        return LoanProduct(self.__request_handler,
                           self.__request_handler.make_request(
                               'GET',
                               '/loanproducts/{}'.format(id)
                           ), False)

    def get_loans(self, **kwargs):
        """
        :calls `GET /loans <https://demo.openmf.org/api-docs/apiLive.htm#loans>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.loan.Loan`
        """
        return PaginatedList(
            Loan,
            self.__request_handler,
            '/loans',
            kwargs
        )

    def get_loan(self, id):
        """
        :calls `GET /loans/<id> <https://demo.openmf.org/api-docs/apiLive.htm#loans_retrieve>`_
        :rtype: :class:`fineract.objects.loan.Loan`
        """
        return Loan(self.__request_handler,
                    self.__request_handler.make_request(
                        'GET',
                        '/loans/{}'.format(id)
                    ), False)

    def get_staff(self, id=None):
        """
        :calls `GET /staff/<id> <https://demo.openmf.org/api-docs/apiLive.htm#staff_retrieve>`_
        :rtype: :class:`fineract.objects.staff.Staff` or  :class:`fineract.pagination.PaginatedList` of
        :class:`fineract.objects.org.Staff`
        """
        if id:
            return Staff(self.__request_handler,
                         self.__request_handler.make_request(
                             'GET',
                             '/staff/{}'.format(id),
                         ), False)
        else:
            return PaginatedList(
                Staff,
                self.__request_handler,
                '/staff',
                dict()
            )

    def get_funds(self, id=None):
        """
        :calls `GET /funds/<id> <https://demo.openmf.org/api-docs/apiLive.htm#funds_retrieve>`_
        :rtype: :class:`fineract.objects.org.Fund` or  :class:`fineract.pagination.PaginatedList` of
        :class:`fineract.objects.org.Fund`
        """
        if id:
            return Fund(self.__request_handler,
                        self.__request_handler.make_request(
                            'GET',
                            '/funds/{}'.format(id),
                        ), False)
        else:
            return PaginatedList(
                Fund,
                self.__request_handler,
                '/funds',
                dict()
            )

    def get_charges(self, id=None):
        """
        :calls `GET /charges/<id> <https://demo.openmf.org/api-docs/apiLive.htm#charges_retrieve>`_
        :rtype: :class:`fineract.objects.org.Charge` or  :class:`fineract.pagination.PaginatedList` of
        :class:`fineract.objects.org.Charge`
        """
        if id:
            return Charge(self.__request_handler,
                          self.__request_handler.make_request(
                              'GET',
                              '/charges/{}'.format(id),
                          ), False)
        else:
            return PaginatedList(
                Charge,
                self.__request_handler,
                '/charges',
                dict()
            )

    def get_offices(self, id=None):
        """
        :calls `GET /offices/<id> <https://demo.openmf.org/api-docs/apiLive.htm#offices_retrieve>`_
        :rtype: :class:`fineract.objects.org.Office` or  :class:`fineract.pagination.PaginatedList` of
        :class:`fineract.objects.org.Office`
        """
        if id:
            return Office(self.__request_handler,
                          self.__request_handler.make_request(
                              'GET',
                              '/offices/{}'.format(id),
                          ), False)
        else:
            return PaginatedList(
                Office,
                self.__request_handler,
                '/offices',
                dict()
            )

    def raw_request(self, method, url, **kwargs):
        """
        Make a raw request to the Fineract API
        :param method:
        :param url:
        :param kwargs:
        :return: Returns dict/list object
        """
        return self.__request_handler.make_request(method, url, **kwargs)
