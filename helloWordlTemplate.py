from flask import Flask, render_template, request, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from devices import devices

from KVMSwitch import KVMSwitch
from SonOffSwitch import SonOffSwitch


# example of a device
# devices = {
#    "Lamp": SonOffSwitch(
#       device_id="AABBCCEEFF",
#       ip_address="0.0.0.0",
#       value="Lamp",
#       name="Lamp",
#       icon="floor_lamp"
#    ),
# }


def check_status():
   # for device in devices.values():
   #    print(device)
   #    device.check_status()
   for key, device in list(filter(lambda obj: isinstance(obj[1], (SonOffSwitch, KVMSwitch)), devices.items())):
      device.check_status()



sched = BackgroundScheduler(daemon=True)
sched.add_job(check_status, 'interval', seconds=5)
sched.start()


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


@app.route("/sunblinds/", methods=['GET', 'POST'])
def sunblinds():
   return render_template("sunblinds.html", device=devices["Balcony"])


@app.route("/<device_id>/rotate_right")
def rotate_right(device_id):
   devices[device_id].rotate_right()
   return "ok"


@app.route("/<device_id>/rotate_left")
def rotate_left(device_id):
   print(device_id)
   devices[device_id].rotate_left()
   return "ok"


@app.route("/<device_id>/stop_rotate")
def stop_rotate(device_id):
   devices[device_id].stop_rotate()
   return "ok"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)