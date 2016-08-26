import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self, app):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, "
                           "homepage from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, homepage) = row
                all_emails = app.contact.merge_emails_like_on_home_page(Contact(email1=email, email2=email2,
                                                                                email3=email3))
                all_phones = app.contact.merge_phones_like_on_home_page(Contact(home_phone=home, mobile_phone=mobile,
                                                                                work_phone=work, fax=fax))
                list.append(Contact(firstname=firstname, lastname=lastname, address=address,
                                    all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones,
                                    homepage=homepage, id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
