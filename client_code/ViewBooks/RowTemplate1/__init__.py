from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.text = anvil.server.call('view_books')
    self.label_1.text = self.item[0]
    self.label_2.text = self.item[1]
    self.label_3.text = self.item[2]
    self.label_4.text = self.item[3]
    self.label_5.text = self.item[4]
    self.label_6.text = self.item[5]
    
    
    
    # Any code you write here will run before the form opens.
