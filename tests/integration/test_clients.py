import filecmp
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


def test_set_image(fineract):
    with open('tests/files/image.png', 'rb') as in_file:
        client = fineract.get_client(1)
        assert client.set_image(in_file, 'image.png')


def test_get_image(fineract, tmpdir):
    in_path = 'tests/files/image.png'
    client = fineract.get_client(1)
    out_file = tmpdir.join('out.png')
    out_path = str(out_file)
    out_file.write_binary(client.download_image())
    assert filecmp.cmp(in_path, out_path)


def test_delete_image(fineract):
    client = fineract.get_client(1)
    assert client.set_image(None, None)


number = random.randint(0, 10000)


def test_client_closure(fineract, fake):
    data = fineract.raw_request('GET', '/clients/template?commandParam=close')
    _id = data['narrations'][-1]['id']
    client = Client.create(fineract.request_handler, fake.first_name(), fake.last_name(), 1,
                           mobile_no='{}'.format(number), middlename=fake.last_name())
    assert client.close(_id)
