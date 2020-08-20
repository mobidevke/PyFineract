import json

import pytest

from fineract.objects.org import Staff, Fund, Charge, Office


@pytest.mark.parametrize('filename, klass', [
    ('staff', Staff),
    ('fund', Fund),
    ('charge', Charge),
    ('office', Office),
])
def test_org_object(filename, klass):
    with open('tests/files/{}.json'.format(filename), 'r') as in_file:
        data = json.load(in_file)
        o = klass(None, data, False)
        assert isinstance(o.id, int)
