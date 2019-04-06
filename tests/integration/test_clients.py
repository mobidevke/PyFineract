import pytest

from fineract import Fineract
from fineract.objects.client import Client


def test_get_all_clients(fineract: Fineract):
    count = len([client for client in fineract.get_clients()])
    assert count == 7


def test_get_all_clients__with_filter(fineract: Fineract):
    count = len([client for client in fineract.get_clients(sqlSearch='c.external_id=11111111')])
    assert count == 1


def test_get_single_client(fineract: Fineract):
    client = fineract.get_client(1)
    assert client


@pytest.mark.parametrize('phone_no, result', [
    ('233717890222', True),
    ('233711111111', False),
])
def test_get_client_by_phone_no(fineract: Fineract, phone_no, result):
    client = Client.get_client_by_phone_no(fineract.request_handler, phone_no)
    assert bool(client) == result


def test_get_client_loans(fineract: Fineract):
    client = fineract.get_client(8)
    assert client
    loans = [loan for loan in client.get_loans()]
    assert len(loans) == 1
