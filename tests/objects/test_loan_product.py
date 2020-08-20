import json

import requests
from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.interest import InterestRecalculationData
from fineract.objects.loan_product import LoanProduct
from fineract.pagination import PaginatedList


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/files/loan_product.json', 'r') as in_file:
                data = json.load(in_file)

            return [data]

    return FakeResponse()


def test_loan_product_object_creation__interest_recalculation_data():
    with open('tests/files/loan_product.json', 'r') as in_file:
        data = json.load(in_file)
        product = LoanProduct(None, data, False)
        assert isinstance(product.interest_recalculation_data, InterestRecalculationData)


def test_get_loan_products(mocker):
    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(LoanProduct, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 1
    assert isinstance(paginated_list[0], LoanProduct)
