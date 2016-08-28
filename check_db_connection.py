# import mysql.connector
import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

# # connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
#
# # -----------------
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()

# # -----------------
#
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass

# -----------------

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id=327))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass