import requests

class Sunblind:
  def __init__(self, ip_address, port, value, name, icon_left, icon_right, show_in_menu):
    self.ip_address = ip_address
    self.port = port
    self.value = value
    self.name = name
    self.show_in_menu = show_in_menu
    self.icon_left = icon_left
    self.icon_right = icon_right

    
  def rotate_right(self):
    json_data = {
      "switch": "on"
    }
    req = requests.post(f"http://{self.ip_address}:{self.port}/right", json=json_data)
  

  def stop_rotate(self):
    json_data = {
      "switch": "off"
    }
    req = requests.post(f"http://{self.ip_address}:{self.port}/right", json=json_data)

  
  def rotate_left(self):
    json_data = {
      "switch": "on"
    }
    req = requests.post(f"http://{self.ip_address}:{self.port}/left", json=json_data)
    
  def check_status():
    pass