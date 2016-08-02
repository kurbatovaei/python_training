# own test group modify cases
from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_editing"))
    app.group.edit_first_group(Group(name="edited_group", header="edited header", footer="edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
