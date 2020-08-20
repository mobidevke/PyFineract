def test_get_all_offices(fineract):
    offices = [office for office in fineract.get_offices()]
    assert len(offices) == 3


def test_get_single_office(fineract):
    office = fineract.get_offices(2)
    assert office
    assert office.name == 'Merida'


def test_get_all_staff(fineract):
    staff = [staff for staff in fineract.get_staff()]
    assert len(staff) == 3


def test_get_single_staff(fineract):
    staff = fineract.get_staff(2)
    assert staff
    assert staff.display_name == 'M, Mary'
