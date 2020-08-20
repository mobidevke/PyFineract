import json

import requests
from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.client import Client, ClientType
from fineract.pagination import PaginatedList


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/files/client.json', 'r') as in_file:
                data = json.load(in_file)

            return [data]

    return FakeResponse()


def test_get_clients(mocker):
    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(Client, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 1
    assert isinstance(paginated_list[0], Client)
    assert isinstance(paginated_list[0].type, ClientType)
