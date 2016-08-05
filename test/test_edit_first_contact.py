from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vladimir", lastname="Putin", address="Russian Federation, Moscow, Kremlin",
                      home_phone="+7 495 697-03-49", mobile_phone="+7 495 697-03-49", work_phone="+7 495 697-03-49",
                      email="mr.president@kremlin.ru")
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_firstname(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
#     app.contact.edit_first_contact(Contact(firstname="Albert"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_first_contact_lastname(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
#     app.contact.edit_first_contact(Contact(lastname="Einstein"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
