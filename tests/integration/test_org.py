def test_get_all_offices(fineract):
    offices = [office for office in fineract.get_offices()]
    assert len(offices) == 3


def test_get_single_office(fineract):
    office = fineract.get_offices(2)
    assert office
    assert office.name == 'Merida'
