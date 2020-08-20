import json

from fineract.objects.currency import Currency


def test_currency_creation():
    with open('tests/files/currency.json', 'r') as in_file:
        data = json.load(in_file)
        curr = Currency(None, data, False)
        assert curr.code == 'USD'
        assert curr.name == 'US Dollar'
        assert curr.decimal_places == 2
        assert curr.in_multiples_of == 0
        assert curr.display_label == 'US Dollar ($)'
        assert curr.display_symbol == '$'
        assert curr.name_code == 'currency.USD'
