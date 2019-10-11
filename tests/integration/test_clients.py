import random

import pytest

from fineract.objects.client import Client
from fineract.objects.document import Document


def test_get_all_clients(fineract):
    count = len([client for client in fineract.get_clients()])
    assert count >= 7


def test_get_all_clients__with_filter(fineract):
    count = len([client for client in fineract.get_clients(sqlSearch='c.mobile_no=233717890222')])
    assert count == 1


def test_get_single_client(fineract):
    client = fineract.get_client(1)
    assert client


@pytest.mark.parametrize('phone_no, result', [
    ('233717890222', True),
    ('233711111111', False),
])
def test_get_client_by_phone_no(fineract, phone_no, result):
    client = Client.get_client_by_phone_no(fineract.request_handler, phone_no)
    assert bool(client) == result


def test_get_client_loans(fineract):
    client = fineract.get_client(8)
    assert client
    loans = [loan for loan in client.get_loans()]
    assert len(loans) == 1


def test_client_creation__basic(fineract, fake):
    client = Client.create(fineract.request_handler, fake.first_name(), fake.last_name(), 1)
    assert client


def test_client_creation__with_optional(fineract, fake):
    number = random.randint(0, 10000)
    client = Client.create(fineract.request_handler, fake.first_name(), fake.last_name(), 1,
                           mobile_no='{}'.format(number), middlename=fake.last_name())
    assert client


def test_updating_client_details(fineract):
    client = fineract.get_client(2)
    client.update({'externalId': 'some-external-id'})
    client = fineract.get_client(2)
    assert client.external_id == 'some-external-id'


def test_client_template_retrieval(fineract):
    template = fineract.templates('clients')
    assert template


def test_client_loans_template_retrieval(fineract):
    template = fineract.templates('loans', 1, 'templateType=individual')
    assert template


def test_add_document(fineract):
    with open('tests/files/image.png', 'rb') as in_file:
        client = fineract.get_client(1)
        doc = client.add_document('Test image', 'Some test description', in_file, 'image.png')
        assert isinstance(doc, Document)


def test_retrieve_all_documents(fineract):
    client = fineract.get_client(1)
    assert client.documents().total_count > 0
