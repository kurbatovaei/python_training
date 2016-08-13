# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    symbols = string.digits + " " + "()" + "+"
    return "".join([random.choice(symbols) for i in range(random.randrange(15))])

testdata = \
    [Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="", email1="")] \
    + \
    [Contact(firstname="Barack", lastname="Obama", address="White House, 1600 Pennsylvania Avenue NW, Washington, D.C.",
             home_phone="202-456-1111", mobile_phone="202-456-1414", work_phone="202-456-2121",
             email1="mr.president@white.house")]\
    + \
    [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
             address=random_string("address", 30), home_phone=random_phone(),
             mobile_phone=random_phone(), work_phone=random_phone(),
             email1=random_string("", 10))
     for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

