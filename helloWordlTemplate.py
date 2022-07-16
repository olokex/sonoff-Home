from flask import Flask, render_template, request
import requests
import json
import sys
sys.path.append('..')
import switcher

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


class KVMSwitch:
   def __init__(self, value, name):
      self.value = value
      self.name = name
      self._check_status()

   def switch_status(self):
      self._check_status()
      switcher.switch_status()      

   def _check_status(self):
      if self.value == "Work":
         self._home()
      else:
         self._work()

   def _work(self):
      self.value = "Work"
      self.style = "btn-off"

   def _home(self):
      self.value = "Home"
      self.style = "btn-on"

devices = {
   "Lamp": SonOffSwitch(
      device_id="100164af39",
      ip_address="192.168.0.127",
      value="Lamp",
      name="Lamp"
   ),

   "Work": KVMSwitch(
      value="Home",
      name="Work"
   ),

}


app = Flask(__name__)

def process_post(site):
   if request.method == 'POST':
      device = request.form["device"]
      print(device)
      if device in devices:
         devices[device].switch_status()

   return render_template(site, devices=devices)


@app.route("/", methods=['GET', 'POST'])
def index():
   return process_post("index.html")


@app.route("/mamka/", methods=['GET', 'POST'])
def mamka():
   return process_post("mamka.html")


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)