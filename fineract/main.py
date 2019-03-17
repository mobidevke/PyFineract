# fineract APIs run on https by default
from fineract.handlers import RequestHandler
from fineract.objects.client import Client
from fineract.objects.loan import Loan
from fineract.objects.loan_product import LoanProduct
from fineract.objects.role import Role
from fineract.pagination import PaginatedList

DEFAULT_BASE_URL = 'https://localhost/fineract-provider/api/v1'
DEFAULT_TENANT = 'default'
DEFAULT_TIMEOUT = 15
DEFAULT_PER_PAGE = 30


class Fineract(object):

    def __init__(self, username=None, password=None, tenant=DEFAULT_TENANT, base_url=DEFAULT_BASE_URL,
                 timeout=DEFAULT_TIMEOUT, per_page=DEFAULT_PER_PAGE, debug=False):
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
        self.__request_handler = RequestHandler(username, password, base_url, tenant, timeout, per_page, debug)

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

    def get_clients(self):
        """
        :calls `GET /clients <https://demo.openmf.org/api-docs/apiLive.htm#clients>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.client.Client`
        """
        return PaginatedList(
            Client,
            self.__request_handler,
            '/clients',
            dict()
        )

    def get_client(self, id):
        """
        :calls `GET /clients/<id> <https://demo.openmf.org/api-docs/apiLive.htm#clients_retrieve>`_
        :rtype: :class:`fineract.objects.client.Client`
        """
        return Client(self.__request_handler,
                      self.__request_handler.make_request(
                          '/clients/{}'.format(id),
                          dict()
                      ), False)

    def get_loan_products(self):
        """
        :calls `GET /loanproducts <https://demo.openmf.org/api-docs/apiLive.htm#loanproducts>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.loan_product.LoanProduct`
        """
        return PaginatedList(
            LoanProduct,
            self.__request_handler,
            '/loanproducts',
            dict()
        )

    def get_loan_product(self, id):
        """
        :calls `GET /loanproducts/<id> <https://demo.openmf.org/api-docs/apiLive.htm#loanproducts_retrieve>`_
        :rtype: :class:`fineract.objects.loan_product.LoanProduct`
        """
        return LoanProduct(self.__request_handler,
                           self.__request_handler.make_request(
                               '/loanproducts/{}'.format(id),
                               dict()
                           ), False)

    def get_loans(self):
        """
        :calls `GET /loans <https://demo.openmf.org/api-docs/apiLive.htm#loans>`_
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.loan.Loan`
        """
        return PaginatedList(
            Loan,
            self.__request_handler,
            '/loans',
            dict()
        )

    def get_loan(self, id):
        """
        :calls `GET /loans/<id> <https://demo.openmf.org/api-docs/apiLive.htm#loans_retrieve>`_
        :rtype: :class:`fineract.objects.loan.Loan`
        """
        return Loan(self.__request_handler,
                    self.__request_handler.make_request(
                        '/loans/{}'.format(id),
                        dict()
                    ), False)
