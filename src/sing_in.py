#!/usr/bin/python3
import cgi
import mysql.connector
from mysql.connector import errorcode

data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')
try:
    cnx = mysql.connector.connect(
        user='user1', password='pass1234', host='127.0.0.1', database='weblogin')
    cursor = cnx.cursor()

    email = data.getvalue('email')
    password = data.getvalue('password')

    query = ("SELECT uname, email FROM users where email = %s and pass = sha1(%s)")

    cursor.execute(query, (email, password))
    record = cursor.fetchone()

    if record:
        print(f'<h1>Bienvenido {record[0]}</h1>')
        print(f'Email {record[1]}')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
