# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="Barack", lastname="Obama",
                               address="White House, 1600 Pennsylvania Avenue NW, Washington, D.C.",
                               home_phone="202-456-1111", mobile_phone="202-456-1414", work_phone="202-456-2121",
                               email="mr.president@white.house"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="",
                               email=""))
    app.logout()
