from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    app.contact.edit_first_contact(Contact(firstname="Vladimir", lastname="Putin",
                                           address="Russian Federation, Moscow, Kremlin", home_phone="+7 495 697-03-49",
                                           mobile_phone="+7 495 697-03-49", work_phone="+7 495 697-03-49",
                                           email="mr.president@kremlin.ru"))


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    app.contact.edit_first_contact(Contact(firstname="Albert"))


def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    app.contact.edit_first_contact(Contact(lastname="Einstein"))
