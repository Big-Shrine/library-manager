from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AddBooks')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('IssueBooks')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ViewBooks')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AddMember')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ViewMember')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ReturnBook')

