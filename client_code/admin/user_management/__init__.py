from ._anvil_designer import user_managementTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_management(user_managementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
   open_form('admin.show_users')

  def button_1_click(self, **event_args):
   open_form('admin.admin_add_user')

  def link_8_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin')

  def link_10_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.user_support')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')
