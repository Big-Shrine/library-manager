from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.visible = False
    self.label_2.visible = False
    def test_mysql_connection():
      try:
        # Attempt to establish a connection
        connection = mysql.connector.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
        # If the connection is successful, print a success message
        self.label_1.visible = True

        # Don't forget to close the connection when you're done
        connection.close()
      except mysql.connector.Error as err:
        # Handle the exception if the connection fails
        self.label_2.visible = True

    test_mysql_connection()
    # Any code you write here will run before the form opens.
