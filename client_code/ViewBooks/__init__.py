from ._anvil_designer import ViewBooksTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewBooks(ViewBooksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.init_components(**properties)
    if type(anvil.server.call('view_books')) == type(''):
      alert(anvil.server.call('view_books'))
    else:
      self.repeating_panel_1.items = anvil.server.call('view_books')
   # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dashboard')
