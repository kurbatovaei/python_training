# own test group modify cases
from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_editing"))
    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    edited_group = Group(name="edited_group", header="edited header", footer="edited footer")
    app.group.edit_group_by_id(group_to_edit.id, edited_group)
    assert len(old_groups) == app.group.count()
    old_groups[group_to_edit.id] = edited_group
    if check_ui:
        assert sorted(db.get_group_list_clean(), key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)
