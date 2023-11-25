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
    self.repeating_panel_1.text = anvil.server.call('view_books')
    self.label_1.text = self.item['BOOK_ID']
    self.label_2.text = self.item['CATEGORY']
    self.label_3.text = self.item['NAME']
    self.label_4.text = self.item['AUTHOR']
    self.label_5.text = self.item['COPIES']
    self.label_6.text = self.item['STATUS']
    # Any code you write here will run before the form opens.
