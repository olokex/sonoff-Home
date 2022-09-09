from flask import Flask, render_template, request, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from devices import devices


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
   for device in devices.values():
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


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)