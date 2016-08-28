from model.group import Group
import random


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_deletion"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_for_deletion"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(db.get_group_list_clean(), key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)
