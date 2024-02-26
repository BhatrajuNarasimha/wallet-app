import anvil.users
from ._anvil_designer import customerTemplate
from anvil import open_form
import datetime


class customer(customerTemplate):
    def __init__(self, user=None, **properties):
        self.init_components(**properties)
        self.user = user  # Set the user attribute
        date = datetime.datetime.now().date()
        if date != self.user['last_login']:
          if self.user['daily_limit_set'] == None:
            self.user['limit']=str(100000)
          else:
            self.user['limit']= self.user['daily_limit_set']
          self.user['last_login']= date
        self.user.update()

        if user:
            # Use the information from the logged-in user
            self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"

    def button_1_click(self, **event_args):
        # Open the Viewprofile form and pass the user information
        open_form('Viewprofile', user=self.user)

    def button_2_click(self, **event_args):
      open_form('wallet', user=self.user)

 

    

    


   

    def link_13_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('Home')

    def link_7_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('withdraw', user=self.user)

    def link_3_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('transfer',user=self.user)

    def link_2_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('deposit', user= self.user)

    def link_8_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

   

   
