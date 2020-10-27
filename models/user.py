"""
Modelo Usuario
"""
from utils.conector import Connector

class User:
    """ clase ususario """
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def login_user(self):
        try:
            conn = Connector()
            cursor = conn.get_cursor()
            query = "SELECT email, name FROM users where email = %s and password = sha1(%s)"
            cursor.execute(query, (self.email, self.password))
            query_result = cursor.fetchone()

            if query_result:
                self.name = query_result[1]
                return True
        except:
            return False
        else:
            conn.close()

    def  query_user(self):
        try:
            conn = Connector()
            cursor = conn.get_cursor()
            query = "SELECT email, name FROM users where email = %s"
            cursor.execute(query, (self.email, self.password))
            query_result = cursor.fetchone()

            if query_result:
                self.name = query_result[1]
                return True
        except:
            return False
        else:
            conn.close()


    def create_user(self):
        try:
            if self.query_user():
                return False
            else:
                conn = Connector()
                cursor = conn.get_cursor()
                add_user = "INSERT INTO users (name, email, password) VALUES (%s, %s, sha1(%s))"
                cursor.execute(add_user, (self.name, self.email, self.password))
                insert_result = cursor.rowcount

                if insert_result:
                    conn.commit()
                    return True
                else:
                    return False
        except:
            return False
        else:
            conn.close()
