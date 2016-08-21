from model.contact import Contact
import random
import string
import json
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
     for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
