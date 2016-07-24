# test group modify cases from lesson_3
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_modification"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_for_modification"))
    app.group.modify_first_group(Group(header="New header"))
