from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import subprocess

# https://github.com/zhaolei/WiringOP with gpio library because i'm unable to make functional pya20

def switch_status():
    # gpio.init()
    # switch = port.PA0
    # gpio.setcfg(switch, gpio.OUTPUT)
    # gpio.output(switch, gpio.HIGH)
    # sleep(0.1)
    # gpio.output(switch, gpio.LOW)
    
    subprocess.run("gpio mode 2 out", shell=True)
    subprocess.run("gpio write 2 1", shell=True)
    sleep(0.1)
    subprocess.run("gpio write 2 0", shell=True)

if __name__ == "__main__":
    switch_status()