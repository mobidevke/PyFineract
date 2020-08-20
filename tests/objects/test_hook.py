import json

import pytest

from fineract.objects.hook import Hook


@pytest.mark.parametrize('filename, klass', [
    ('hook', Hook),
])
def test_hook_object(filename, klass):
    with open('tests/files/{}.json'.format(filename), 'r') as in_file:
        data = json.load(in_file)
        o = klass(None, data, False)
        assert isinstance(o.id, int)
        assert isinstance(o.config, list)
        assert isinstance(o.events, list)
        assert o.events
        assert o.config
