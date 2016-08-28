from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    old_contacts = db.get_contact_list(app)
    contact_to_edit = random.choice(old_contacts)
    edited_contact = Contact(firstname="Vladimir", lastname="Putin", address="Russian Federation, Moscow, Kremlin",
                             home_phone="+7 495 697-03-49", mobile_phone="+7 495 697-03-49",
                             work_phone="+7 495 697-03-49", email1="mr.president@kremlin.ru")
    app.contact.edit_contact_by_id(contact_to_edit.id, edited_contact)
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == \
               sorted(db.get_contact_list_clean(app), key=Contact.id_or_max)


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
