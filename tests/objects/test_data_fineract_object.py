import pytest

from fineract.handlers import RequestHandler
from fineract.objects.fineract_object import DataFineractObject


def test_attribute_error_raised_for_missing_id():
    with pytest.raises(AttributeError):
        o = DataFineractObject(None, {}, False)
        o.get_datatable_data('some_data_table')


def test_get_datatable_data_returns_data(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost/', 'default', per_page=10, timeout=30)
    mocker.patch.object(request_handler, 'make_request', return_value=[])
    o = DataFineractObject(request_handler, {}, False)
    setattr(o, 'id', 1)
    result = o.get_datatable_data('some_data_table')
    assert result == []


def test_request_handler_is_inherited():
    request_handler = RequestHandler('a', 'b', 'https://localhost/', 'default', per_page=10, timeout=30)
    o = DataFineractObject(request_handler, {}, False)
    assert o.request_handler
