import pytest

from fineract import Fineract
from fineract.handlers import RequestHandler


@pytest.mark.parametrize('params', [
    {'username': 1},
    {'password': 1},
    {'tenant': 1},
    {'base_url': 1},
])
def test_error_raised_when_invalid_params_are_passed(params):
    with pytest.raises(AssertionError):
        Fineract(**params)


def test_request_handler_initialized():
    f = Fineract()
    assert isinstance(f._Fineract__request_handler, RequestHandler)
