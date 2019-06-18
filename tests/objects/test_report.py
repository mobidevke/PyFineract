import json

import pytest

from fineract.objects.report import Report


@pytest.mark.parametrize('filename, klass', [
    ('report', Report),
])
def test_org_object(filename, klass):
    with open('tests/files/{}.json'.format(filename), 'r') as in_file:
        data = json.load(in_file)
        o = klass(None, data, False)
        assert isinstance(o.id, int)
        assert isinstance(o.report_parameters, list)
