from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, all_phones_from_home_page=None, email1=None, email2=None, email3=None,
                 all_emails_from_home_page=None, homepage=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.home_phone, self.mobile_phone,
                                            self.work_phone, self.email1, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
