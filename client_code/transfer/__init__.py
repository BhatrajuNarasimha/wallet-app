from ._anvil_designer import transferTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class transfer(transferTemplate):
    def __init__(self, user=None, **properties):
        self.user = user
        self.init_components(**properties)
        self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
        
   

    def button_5_click(self, **event_args):
      open_form('transfer.transaction_history',user= self.user)

    def button_4_click(self, **event_args):
      open_form('transfer.e_wallet_to_accounts', user= self.user)

    def outlined_button_1_click(self, **event_args):
      open_form('transfer.account_to_ewallet',user = self.user)

    def button_3_click(self, **event_args):
      open_form('transfer.e_wallet_to_e_wallet', user= self.user)

    def outlined_button_2_click(self, **event_args):
      open_form('transfer.auto_top_up',user= self.user)

    def outlined_button_3_click(self, **event_args):
      open_form('transfer.set',user= self.user)

    def link_2_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("deposit",user=self.user)

    def link_3_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("transfer",user=self.user)

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("withdraw",user=self.user)

    def link_7_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

    def link_1_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("customer",user=self.user)

    def link_13_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("Home")

    def link_8_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

    

  

    

    

    
       
      

    
              
