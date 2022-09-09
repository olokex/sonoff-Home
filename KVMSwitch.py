import Switcher

class KVMSwitch:
   def __init__(self, value, name, icon):
      self.value = value
      self.name = name
      self.icon = icon
      self._check_status()

   def check_status(self):
      pass

   def switch_status(self):
      self._check_status()
      # Switcher.switch_status()      

   def _check_status(self):
      if self.value == "Work":
         self._home()
      else:
         self._work()

   def _work(self):
      self.value = "Work"
      self.style = "btn-off"
      self.icon = "business_center"

   def _home(self):
      self.value = "Home"
      self.style = "btn-on"
      self.icon = "scene"
