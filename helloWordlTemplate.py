from flask import Flask, render_template, request, redirect, url_for
from SonOffSwitch import SonOffSwitch
from KVMSwitch import KVMSwitch


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

   "Fan": SonOffSwitch(
      device_id="100164af39",
      ip_address="192.168.0.127",
      value="Fan",
      name="Fan"
   ),

}


app = Flask(__name__)


def process_post(site):
   if request.method == 'POST':
      device = request.form["device"]
      if device in devices:
         devices[device].switch_status()
      return redirect(request.url, code=303)
   else:
      return render_template(site, devices=devices)


@app.route("/", methods=['GET', 'POST'])
def index():
   return process_post("index.html")


@app.route("/mamka/", methods=['GET', 'POST'])
def mamka():
   return process_post("mamka.html")


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)