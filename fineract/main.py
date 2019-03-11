# fineract APIs run on https by default
from fineract.handlers import RequestHandler

DEFAULT_BASE_URL = 'https://localhost/fineract-provider/api/v1'
DEFAULT_TENANT = 'default'
DEFAULT_TIMEOUT = 15


class Fineract(object):

    def __init__(self, username=None, password=None, tenant=DEFAULT_TENANT, base_url=DEFAULT_BASE_URL,
                 timeout=DEFAULT_TIMEOUT):
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
        self.__request_handler = RequestHandler(username, password, base_url, tenant, timeout)
