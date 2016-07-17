# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login("admin", "secret")
        self.app.create_contact(Contact(firstname="Barack", lastname="Obama",
                                    address="White House, 1600 Pennsylvania Avenue NW, Washington, D.C.",
                                    home_phone="202-456-1111", mobile_phone="202-456-1414",
                                    work_phone="202-456-2121", email="mr.president@white.house"))
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login("admin", "secret")
        self.app.create_contact(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="",
                                    work_phone="", email=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
