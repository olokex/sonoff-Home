import requests
import json

class SonOffSwitch:
   def __init__(self, device_id, ip_address, value, name):
      self.device_id = device_id
      self.ip_address = ip_address
      self.value = value
      self.name = name
      self.check_status()

   def _send_request(self, message=None, address=None):
      msg = {
         "deviceid": self.device_id,
         "data": { 
            "switch": self.status
         }
      }
      
      response = requests.post("http://{}:8081/zeroconf/switch".format(self.ip_address), json=msg)
      print(response)

   def check_status(self):
      msg = {
         "deviceid": self.device_id,
         "data": { }
      }
   
      response = requests.post("http://{}:8081/zeroconf/info".format(self.ip_address), json=msg)
      response = json.loads(response.content)

      if response["data"]["switch"] == "off":
         self._off()
      else:
         self._on()

   def _on(self):
      self.status = "on"
      self.style = "btn-on"

   def _off(self):
      self.status = "off"
      self.style = "btn-off"

   def switch_status(self):
      if self.status == "off":
         self._on()
      else:
         self._off()
      self._send_request()