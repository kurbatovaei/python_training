from model.contact import Contact
from random import randrange


def test_random_contact_info_on_home_page(app):
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


def test_all_contact_info_with_db(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ernest", lastname="Hemingway",
                                   address="907 Whitehead St, Key West, FL 33040", email1="Ernest.Hemingway@gmail.com",
                                   email2="Ernest.Hemingway@florida.com", email3="Ernest.Hemingway@keywest.com",
                                   home_phone="(305)294-1136", mobile_phone="+1(305)509-1876",
                                   work_phone="(305)294 1575", fax="305 294-2755",
                                   homepage="http://www.hemingwayhome.com/"))
    # get contact list from homepage
    contacts_from_homepage = app.contact.get_contact_list()
    # get contact list from db
    contacts_from_db = db.get_contact_list(app)
    # sort lists and check they are equal
    contacts_from_homepage_sorted = sorted(contacts_from_homepage, key=Contact.id_or_max)
    contacts_from_db_sorted = sorted(contacts_from_db, key=Contact.id_or_max)
    assert contacts_from_homepage_sorted == contacts_from_db_sorted

    def check_contact(contact_from_homepage, contact_from_db):
        assert contact_from_homepage.firstname == contact_from_db.firstname
        assert contact_from_homepage.lastname == contact_from_db.lastname
        assert contact_from_homepage.address == contact_from_db.address
        print("\n>>>>hp....%s" % contact_from_homepage)
        print("\n>>>>hp....%s" % contact_from_db)
        assert contact_from_homepage.all_emails_from_home_page == contact_from_db.all_emails_from_home_page
        assert contact_from_homepage.all_phones_from_home_page == contact_from_db.all_phones_from_home_page

    [check_contact(contacts_from_homepage_sorted[i], contacts_from_db_sorted[i]) for i in
     range(len(contacts_from_homepage))]
