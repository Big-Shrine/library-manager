from ._anvil_designer import ReturnBookTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ReturnBook(ReturnBookTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer_id=int(self.text_box_1.text)
    book_id=int(self.text_box_2.text)
    result_message = anvil.server.call('return_books', customer_id, book_id)
    alert(result_message)
    if result_message == 'Book returned successfully':
      self.text_box_1.text=''
      self.text_box_2.text=''

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dashboard')