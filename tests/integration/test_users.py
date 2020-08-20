def test_get_all_users(fineract):
    users = [user for user in fineract.get_users()]
    assert len(users) > 1


def test_get_single_user(fineract):
    users = fineract.get_users()
    assert fineract.get_users(users[0].id)