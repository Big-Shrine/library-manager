from ._anvil_designer import AddMemberTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddMember(AddMemberTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name.text
    email = self.email.text
    phone_number = self.phonenumber.text
    address = self.address.text
    result_message=anvil.server.call('addCustomer', name, email, phone_number, address)
    alert(result_message)
    if result_message == "Customer added successfully":
      self.name.text=''
      self.email.text=''
      self.phonenumber.text=''
      self.address.text=''

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dashboard')
      
    
