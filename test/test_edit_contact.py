from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Vladimir", lastname="Putin", address="Russian Federation, Moscow, Kremlin",
                      home_phone="+7 495 697-03-49", mobile_phone="+7 495 697-03-49", work_phone="+7 495 697-03-49",
                      email1="mr.president@kremlin.ru")
    app.contact.edit_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
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
