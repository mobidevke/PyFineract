import random

from fineract.objects.group import Group

number = random.randint(0, 10000)


def test_create_group(fineract):
    group = Group.create(fineract.request_handler, 'Test ' + str(number), 1)
    assert isinstance(group, Group)


def test_get_group_by_name(fineract):
    group = Group.get_group_by_name(fineract.request_handler, 'Test ' + str(number))
    assert isinstance(group, Group)


def test_add_member_to_group(fineract):
    client = fineract.get_client(1)
    group = Group.get_group_by_name(fineract.request_handler, 'Test ' + str(number))
    assert group.add_members([client.id])


def test_remove_member_from_group(fineract):
    client = fineract.get_client(1)
    group = Group.get_group_by_name(fineract.request_handler, 'Test ' + str(number))
    assert group.remove_members([client.id])
