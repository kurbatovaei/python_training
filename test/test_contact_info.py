from model.contact import Contact
from random import randrange


def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway",
                                   address="907 Whitehead St, Key West, FL 33040", email1="Ernest.Hemingway@gmail.com",
                                   email2="Ernest.Hemingway@florida.com", email3="Ernest.Hemingway@keywest.com",
                                   home_phone="(305)294-1136", mobile_phone="+1(305)509-1876",
                                   work_phone="(305)294 1575", fax="305 294-2755",
                                   homepage="http://www.hemingwayhome.com/"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
        contact_from_edit_page)
