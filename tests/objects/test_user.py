import json

import pytest

from fineract.objects.user import User


@pytest.mark.parametrize('filename, klass', [
    ('user', User),
])
def test_report_object(filename, klass):
    with open('tests/files/{}.json'.format(filename), 'r') as in_file:
        data = json.load(in_file)
        o = klass(None, data, False)
        assert isinstance(o.id, int)
        assert isinstance(o.selected_roles, list)
