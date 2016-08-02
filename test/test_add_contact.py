# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Barack", lastname="Obama",
                               address="White House, 1600 Pennsylvania Avenue NW, Washington, D.C.",
                               home_phone="202-456-1111", mobile_phone="202-456-1414", work_phone="202-456-2121",
                               email="mr.president@white.house"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="",
                               email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
