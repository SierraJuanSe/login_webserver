#!/usr/bin/python3
import cgi
data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')

name = data.getvalue('name')
email = data.getvalue('email')
password = data.getvalue('password')

print(f'Welcome {name} {email} {password}')
