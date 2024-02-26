from ._anvil_designer import show_usersTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class show_users(show_usersTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Set the visibility of the button to False
        self.button_1.visible = False
       

        # Filter users and set items in the repeating panel
        self.refresh_users()

    def refresh_users(self, username_filter=None):
        # If a username filter is provided, filter users based on the username
        if username_filter:
            customer_type_filter = [user for user in app_tables.users.search()
                                    if user['usertype'] == 'customer' and user['username'].lower().startswith(username_filter.lower())]
        else:
            # If no username filter, show all customers
            customer_type_filter = [user for user in app_tables.users.search() if user['usertype'] == 'customer']

        # Set items in the repeating panel
        self.repeating_panel_1.items = customer_type_filter

    def button_1_click(self, **event_args):
        # Toggle visibility of the repeating panel
        self.repeating_panel_1.visible = not self.repeating_panel_1.visible

    def button_2_click(self, **event_args):
        # Handle search button click event to refresh users based on entered username
        username_filter = self.text_box_1.text
        self.refresh_users(username_filter)

    def button_8_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('Home')

    def link_10_copy_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('admin.user_support')

    def link_8_copy_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('admin')
