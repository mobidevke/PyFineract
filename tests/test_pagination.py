import json

import requests
from requests import Response
from six.moves.urllib_parse import urlparse, parse_qs

from fineract.handlers import RequestHandler
from fineract.objects.fineract_object import FineractObject
from fineract.pagination import PaginatedList, PaginatedList2


def fake_handler1(self, req, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/clients.json', 'r') as in_file:
                data = json.load(in_file)

            return data

    return FakeResponse()


def fake_handler2(self, req, **kwargs):
    parsed = urlparse(req.url)
    params = parse_qs(parsed.query)
    params = {key: val[0] for key, val in params.items()}

    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs1):
            with open('tests/clients.json', 'r') as in_file:
                data = json.load(in_file)

            offset = int(params.get('offset', 0))
            limit = int(params.get('limit', 30))

            items = []

            count = 0
            for item in data[offset:]:
                if count == limit:
                    break

                items.append(item)
                count += 1

            return {
                'totalFilteredRecords': len(data),
                'pageItems': items
            }

    return FakeResponse()


def test_total_count__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_total_count__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_full_iteration__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 10


def test_partial_iteration__no_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 5


def test_full_iteration__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 5)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for _ in paginated_list:
        count += 1

    assert count == 5


def test_partial_iteration__with_pagination(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 3)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 3


def test_get_page(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 2)
    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList(FineractObject, request_handler, '/', {})
    items = paginated_list.get_page(1)
    assert len(items) == 2


def test_total_count__no_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_has_next__no_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    assert not paginated_list.has_next()


def test_total_count__with_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    assert paginated_list.total_count == 10


def test_full_iteration__no_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 10


def test_partial_iteration__no_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 5


def test_full_iteration__with_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 5)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    count = 0
    for _ in paginated_list:
        count += 1

    assert count == 5


def test_partial_iteration__with_pagination2(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 3)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    count = 0
    for item in paginated_list[:5]:
        count += 1

    assert count == 3


def test_full_iteration__with_pagination__all_pages(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 5)

    mocker.patch.object(requests.Session, 'send', new=fake_handler2)
    paginated_list = PaginatedList2(FineractObject, request_handler, '/', {})
    count = 0

    while paginated_list.has_next():
        for _ in paginated_list:
            count += 1

        paginated_list.get_next()

    assert count == 10
