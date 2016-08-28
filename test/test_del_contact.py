from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list(app)) == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    old_contacts = db.get_contact_list(app)
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list(app)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == \
               sorted(db.get_contact_list_clean(app), key=Contact.id_or_max)

