from model.contact import Contact
import random


def test_delete_contact(app, db):
    if len(db.get_contact_list(app)) == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    old_contacts = db.get_contact_list(app)
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list(app)
    assert old_contacts == new_contacts
