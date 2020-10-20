#!/usr/bin/python3
import cgi
import mysql.connector


data = cgi.FieldStorage()
print('Content-Type: text/html')
print('')
try:
    cnx = mysql.connector.connect(
        user='user1', password='pass1234', host='127.0.0.1', database='weblogin')
    cursor = cnx.cursor()

    name = data.getvalue('name')
    email = data.getvalue('email')
    password = data.getvalue('password')

    add_user = ("INSERT INTO users "
                "(uname, email, pass) "
                "VALUES (%s, %s, sha1(%s))")
    data_user = (name, email, password)

    cursor.execute(add_user, data_user)
    user_no = cursor.lastrowid
    cnx.commit()

    print('<h1>Usuario registrado</h1>')
    if user_no:
        print('Usuario registrado')
        query = ("SELECT * FROM users where email = %s and pass = sha1(%s)")

        cursor.execute(query, (email, password))
        record = cursor.fetchone()

        print(record)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
