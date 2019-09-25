import json

import pytest

from fineract.objects.datatable import DataTable


@pytest.mark.parametrize('filename, klass', [
    ('datatable', DataTable),
])
def test_report_object(filename, klass):
    with open('tests/files/{}.json'.format(filename), 'r') as in_file:
        data = json.load(in_file)
        o = klass(None, data, False)
        assert isinstance(o.application_table_name, str)
        assert isinstance(o.column_header_data, list)
