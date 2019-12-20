import random

import pytest

from fineract import FineractException
from fineract.objects.datatable import DataTable

number = random.randint(0, 10000)


def test_create_datatable(fineract):
    columns = [
        {
            'name': 'Test',
            'length': 100,
            'type': 'String',
            'mandatory': False
        },
        {
            'name': 'Time',
            'type': 'DateTime',
            'mandatory': False
        }
    ]
    datatable = DataTable.create(fineract.request_handler, 'datatable {}'.format(number), DataTable.CLIENT, columns)
    assert isinstance(datatable, DataTable)


def test_get_datatable(fineract):
    assert DataTable.get(fineract.request_handler, 'datatable {}'.format(number))


def test_update_datatable(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    datatable.update(apptable_name=DataTable.LOAN)
    assert datatable.application_table_name == DataTable.LOAN


def test_update_datatable_columns(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    with pytest.raises(FineractException):
        datatable.update(add_columns=[
            {
                'name': 'Test',
                'type': 'Text'
            }
        ])


def test_datatable_deletion(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    assert datatable.delete()


def test_data_insertion(fineract):
    columns = [
        {
            'name': 'Test',
            'length': 100,
            'type': 'String'
        }
    ]
    datatable = DataTable.create(fineract.request_handler, 'datatable {}'.format(number), DataTable.CLIENT, columns)
    assert isinstance(datatable, DataTable)
    assert datatable.insert(1, {'Test': 'test value'})


def test_get_data(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    data = datatable.get_data(1)
    assert data == [{'client_id': 1, 'Test': 'test value'}]


def test_data_update(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    datatable.update_data(1, {'Test': 'test value 2'})
    data = datatable.get_data(1)
    assert data == [{'client_id': 1, 'Test': 'test value 2'}]


def test_data_deletion(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    assert datatable.delete_data(1)


def test_data_insertion_multirow(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    datatable.delete()
    columns = [
        {
            'name': 'Test',
            'length': 100,
            'type': 'String'
        }
    ]
    datatable = DataTable.create(fineract.request_handler, 'datatable {}'.format(number), DataTable.CLIENT, columns,
                                 True)
    assert isinstance(datatable, DataTable)
    assert datatable.insert(1, {'Test': 'test value'})
    assert datatable.insert(1, {'Test': 'test value 2'})


def test_get_data_multirow(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    data = datatable.get_data(1)
    print(data)
    assert data == [{'id': 1, 'client_id': 1, 'Test': 'test value'}, {'id': 2, 'client_id': 1, 'Test': 'test value 2'}]


def test_data_update_multirow(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    datatable.update_data(1, {'Test': 'test value 3'}, 2)
    data = datatable.get_data(1)
    assert data == [{'id': 1, 'client_id': 1, 'Test': 'test value'}, {'id': 2, 'client_id': 1, 'Test': 'test value 3'}]


def test_data_deletion__multirow(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    datatable.delete_data(1, 2)
    data = datatable.get_data(1)
    assert data == [{'id': 1, 'client_id': 1, 'Test': 'test value'}]