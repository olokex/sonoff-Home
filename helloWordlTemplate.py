from flask import Flask, render_template, request
import datetime
import requests

devices = {
   "Lamp": {
      "deviceid": "100164af39",
      "data": { 
        "switch": "off"
      },
      "style": "btn-off"
   },
   "Work": {
      "deviceid": "100164af39",
      "data": { 
        "switch": "off"
      },
      "style": "btn-off",
   },
   "Fan": {
      "deviceid": "100164af39",
      "data": { 
        "switch": "off"
      },
      "style": "btn-off"
   }
}

def send_request(data):
   status = data['data']['switch']

   if data['data']['switch'] == 'off':
      data['data']['switch'] = 'on'
      data['style'] = 'btn-on'
   else:
      data['data']['switch'] = 'off'
      data['style'] = 'btn-off'

   print(data)
   # req = requests.post("http://192.168.0.127:8081/zeroconf/switch", json=data)
   # print(req)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
   templateData = {
      'time': "Hello Simi",
      'devices': devices
   }

   if request.method == 'POST':
      submited = request.form.to_dict(flat=False)
      key = submited.popitem()[0]
      send_request(devices[key])

   return render_template("index.html", **templateData)

@app.route("/mamka/", methods=['GET', 'POST'])
def mamka():
   templateData = {
      'devices': devices
   }

   if request.method == 'POST':
      submited = request.form.to_dict(flat=False)
      key = submited.popitem()[0]
      send_request(devices[key])

   return render_template("mamka.html", **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)