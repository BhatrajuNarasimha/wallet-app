from ._anvil_designer import customerTemplate
from anvil import *
import anvil.server

class customer(customerTemplate):
  def __init__(self, user=None, **properties):
        self.init_components(**properties)

        if user:
            # Use the information from the logged-in user
            self.label_1.text = f"{user['username']}!"
