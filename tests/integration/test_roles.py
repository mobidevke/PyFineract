def test_get_all_roles(fineract):
    roles = [role for role in fineract.get_roles()]
    assert len(roles) == 1
