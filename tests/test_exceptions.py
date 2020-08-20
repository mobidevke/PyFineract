from fineract import FineractException


def test_exception_status():
    e = FineractException(400, None)
    assert e.status == 400


def test_exception_data():
    e = FineractException(400, None)
    assert e.data is None


def test_str_representation():
    e = FineractException(400, None)
    assert str(e) == '400 None'
