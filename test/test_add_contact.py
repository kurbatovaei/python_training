# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Barack", lastname="Obama",
                               address="White House, 1600 Pennsylvania Avenue NW, Washington, D.C.",
                               home_phone="202-456-1111", mobile_phone="202-456-1414", work_phone="202-456-2121",
                               email="mr.president@white.house"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="",
                               email=""))
