from ._anvil_designer import user_supportTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_support(user_supportTemplate):
  def __init__(self, serves_data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if serves_data is not None:
            # Bind the data to the Repeating Panel
     self.repeating_panel_1.items = serves_data

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('LOGIN')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def link_10_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.user_support')

  def link_8_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin')
