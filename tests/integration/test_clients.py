import random

import pytest

from fineract.objects.client import Client


def test_get_all_clients(fineract):
    count = len([client for client in fineract.get_clients()])
    assert count >= 7


def test_get_all_clients__with_filter(fineract):
    count = len([client for client in fineract.get_clients(sqlSearch='c.external_id=11111111')])
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
    client = Client.create(fineract.request_handler, fake.first_name(), fake.last_name(), 1, mobile_no='{}'.format(number))
    assert client
