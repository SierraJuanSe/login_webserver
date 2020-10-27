#!/usr/bin/python3
import cgi
from models.user import User

data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')


try:
    user = User("", data.getvalue('email'), data.getvalue('password'))

    if user.create_user():
        page = open('./templates/goodSingIn.html', "r")
        print(page.read())
    else:
        page = open('./templates/errorSingIn.html', "r")
        print(page.read())

except:
    page = open('./templates/errorSingIn.html', "r")
    print(page.read())