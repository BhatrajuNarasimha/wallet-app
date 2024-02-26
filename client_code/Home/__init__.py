from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   

 

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('LOGIN')

  def image_1_copy_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_14.visible=True
    self.spacer_7.visible=False

  def image_1_copy_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_14.visible=False
    self.spacer_7.visible=True

  def image_17_copy_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_13.visible=True
    self.spacer_5.visible=False

  def image_17_copy_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_13.visible=False
    self.spacer_5.visible=True

  def image_17_copy_2_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_13_copy.visible=True
    self.spacer_6.visible=False

  def image_17_copy_2_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_13_copy.visible=False
    self.spacer_6.visible=True

  def image_19_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_5.visible=True
    self.spacer_1.visible=False

  def image_19_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_5.visible=False
    self.spacer_1.visible=True

  def image_20_copy_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_9.visible=True
    self.spacer_1.visible=False

  def image_20_copy_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_9.visible=False
    self.spacer_1.visible=True

  def image_21_copy_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_15.visible=True
    self.spacer_1.visible=False

  def image_21_copy_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_15.visible=False
    self.spacer_1.visible=True

  def image_2_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_19.visible=True
    self.spacer_8.visible=False

  def image_2_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_19.visible=False
    self.spacer_8.visible=True

  def image_5_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_20.visible=True
    self.spacer_8.visible=False

  def image_5_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_20.visible=False
    self.spacer_8.visible=True

  def image_4_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    self.label_21.visible=True
    self.spacer_8.visible=False

  def image_4_mouse_leave(self, x, y, **event_args):
    """This method is called when the mouse cursor leaves this component"""
    self.label_21.visible=False
    self.spacer_8.visible=True

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("LOGIN")

