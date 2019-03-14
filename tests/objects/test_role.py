import json

from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.role import Role
from fineract.pagination import PaginatedList

ROLES = [
    {
        'id': 1,
        'name': 'role 1',
        'description': 'some description'
    },
    {
        'id': 2,
        'name': 'role 2',
        'description': 'some description'
    }
]


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/files/loan_product.json', 'r') as in_file:
                data = json.load(in_file)

            return ROLES

    return FakeResponse()


def test_get_loan_roles(mocker):
    mocker.patch('requests.request', new=fake_handler1)
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch('requests.request', new=fake_handler1)
    paginated_list = PaginatedList(Role, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 2
    assert isinstance(paginated_list[0], Role)


def test__repr__():
    data = ROLES[0]
    role = Role(None, data, False)
    assert repr(role) == 'Role(name="role 1")'
