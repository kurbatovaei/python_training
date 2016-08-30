from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list(app)) == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_to_add_contact"))

    def choose_random_contact():
        contacts = db.get_contact_list(app)
        return random.choice(contacts)

    def choose_random_group():
        groups = db.get_group_list()
        return random.choice(groups)

    contact = None
    orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    while contact is None:
        contact = choose_random_contact()
        group = choose_random_group()
        old_contacts = orm_db.get_contacts_in_group(group)
        if contact not in old_contacts:
            app.contact.add_contact_to_group(app, contact, group)
            new_contacts = orm_db.get_contacts_in_group(group)
            old_contacts.append(contact)
            assert sorted(new_contacts, key=Group.id_or_max) == sorted(old_contacts, key=Group.id_or_max)
        else:
            contact = None


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list(app)) == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_to_delete_contact"))

    def choose_random_contact():
        contacts = db.get_contact_list(app)
        return random.choice(contacts)

    def choose_random_group():
        groups = db.get_group_list()
        return random.choice(groups)

    group = choose_random_group()
    orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_init = orm_db.get_contacts_in_group(group)

    if len(old_contacts_init) > 0:
        contact = random.choice(old_contacts_init)
        app.contact.remove_contact_from_group(app, contact, group)
    else:
        old_contacts = orm_db.get_contacts_in_group(group)
        contact = choose_random_contact()
        app.contact.add_contact_to_group(app, contact, group)
        new_contacts = orm_db.get_contacts_in_group(group)
        old_contacts.append(contact)
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(old_contacts, key=Group.id_or_max)
        app.contact.remove_contact_from_group(app, contact, group)
        new_contacts.remove(contact)
        assert sorted(old_contacts_init, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
