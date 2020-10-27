#!/usr/bin/python3
import cgi
from models.user import User

data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')


try:
    user = User(data.getvalue('name'), data.getvalue('email'), data.getvalue('password'))

    if user.create_user():
        page = open('./templates/goodSingUp.html', "r")
        print(page.read())
    else:
        page = open('./templates/errorSingUp.html', "r")
        print(page.read())

except:
    page = open('./templates/errorSingUp.html', "r")
    print(page.read())