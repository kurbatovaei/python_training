# own test group modify cases
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_editing"))
    app.group.edit_first_group(Group(name="edited_group", header="edited header", footer="edited footer"))
