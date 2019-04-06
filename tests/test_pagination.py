import json

from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.fineract_object import FineractObject
from fineract.pagination import PaginatedList


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/clients.json', 'r') as in_file:
                data = json.load(in_file)

            return data

    return FakeResponse()


def fake_handler2(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs1):
            with open('tests/clients.json', 'r') as in_file:
                data = json.load(in_file)
            params = kwargs.get('params', {})
            offset = params.get('offset', 0)
            limit = params.get('limit', 30)

            return {
                'totalFilteredRecords': len(data),
                'pageItems': data[offset:limit]
            }

    return FakeResponse()


def test_total_count__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch('requests.request', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_total_count__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch('requests.request', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_full_iteration__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch('requests.request', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 10


def test_partial_iteration__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch('requests.request', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 5


def test_full_iteration__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 5)

    mocker.patch('requests.request', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 5


def test_partial_iteration__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 3)

    mocker.patch('requests.request', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 3


def test_get_page(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 2)
    mocker.patch('requests.request', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    items = paginated_list.get_page(1)
    assert len(items) == 2
