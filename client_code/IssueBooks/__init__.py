from ._anvil_designer import IssueBooksTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class IssueBooks(IssueBooksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer=self.customer.text
    bookid=self.bookid.text
    datetime=self.datetime.text
    result_message=anvil.server.call('issueBooks', customer, bookid, datetime)
    alert(result_message)
    if result_message=="Book issued successfully":
      open_form('Dashboard')
      
    
