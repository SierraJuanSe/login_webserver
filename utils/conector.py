"""
Conector de la base de datos mysql
"""
import mysql.connector
from mysql.connector import errorcode


class Connector:
  """Clase conector"""
  def __init__(self, user='webuser', password='pass1234', host='127.0.0.1', database='weblogin'):
    try:
      self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
        self.cnx = -1
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
        self.cnx = 0
      else:
        print(err)
        self.cnx = -2

  def get_connector(self):
    return self.cnx

  
  def get_cursor(self):
    return self.cnx.cursor()
  
  def commit(self):
    self.cnx.commit()

  def close(self):
    self.cnx.close()
