import random

from fineract.objects.datatable import DataTable

number = random.randint(0, 10000)


def test_create_datatable(fineract):
    columns = [
        {
            'name': 'Test',
            'length': 100,
            'type': 'String'
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


def test_datatable_deletion(fineract):
    datatable = DataTable.get(fineract.request_handler, 'datatable {}'.format(number))
    assert datatable.delete()
