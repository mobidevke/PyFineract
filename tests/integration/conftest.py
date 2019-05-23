import pytest
from faker import Faker

from fineract import Fineract


@pytest.fixture(scope='session')
def fineract():
    f = Fineract(
        username='fincore',
        password='password',
        base_url='https://localhost:8443/fineract-provider/api/v1/',
        per_page=100,
        debug=True,
        ssl_check=False
    )
    yield f


@pytest.fixture(scope='session')
def fake():
    return Faker()