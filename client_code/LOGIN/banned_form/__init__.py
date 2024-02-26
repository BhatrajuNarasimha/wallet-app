from ._anvil_designer import banned_formTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class banned_form(banned_formTemplate):
  def __init__(self,user=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = user

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('withdraw',user=self.user)

  
