import json

import requests
from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.group import Group
from fineract.pagination import PaginatedList


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/files/group.json', 'r') as in_file:
                data = json.load(in_file)

            return [data]

    return FakeResponse()


def test_get_groups(mocker):
    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(Group, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 1
    assert isinstance(paginated_list[0], Group)
