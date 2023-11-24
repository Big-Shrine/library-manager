from ._anvil_designer import AddBooksTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddBooks(AddBooksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    bkid=self.bookid2.text
    gre=self.genre.text
    bkname=self.bookname.text
    auth=self.author.text
    copies=int(self.copies.text)
    result_message=anvil.server.call('addBook', bkid, gre, bkname, auth, copies)
    alert(result_message)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dashboard')
