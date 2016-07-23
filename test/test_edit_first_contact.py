from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="Vladimir", lastname="Putin",
                                           address="Russian Federation, Moscow, Kremlin", home_phone="+7 495 697-03-49",
                                           mobile_phone="+7 495 697-03-49", work_phone="+7 495 697-03-49",
                                           email="mr.president@kremlin.ru"))
    app.session.logout()


def test_edit_first_contact_firstname(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="Albert"))
    app.session.logout()


def test_edit_first_contact_lastname(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(lastname="Einstein"))
    app.session.logout()
