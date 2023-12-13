from ._anvil_designer import ItemTemplate6Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate6(ItemTemplate6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
        # Access the data for the selected user
        selected_user = self.item  # Assuming you have set the 'item' property of the repeating panel to the user row
        
        # Open the admin_view form and pass the user details
        open_form('admin.admin_view', user_data=selected_user)

    # Any code you write here will run before the form opens.
