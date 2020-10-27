#!/usr/bin/python3
import cgi
import codecs
from models.user import User

data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')


try:
    user = User("", data.getvalue('email'), data.getvalue('password'))

    if user.query_user():
        page = codecs.open('./templates/goodSingIn.html', "r", "utf-8")
        print(page.read())
    else:
        page = codecs.open('./templates/errorSingIn.html', "r", "utf-8")
        print(page.read())

except:
    page = codecs.open('./templates/errorSingIn.html', "r", "utf-8")
    print(page.read())

