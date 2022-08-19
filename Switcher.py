from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

def switch_status():
    #initialize the gpio module
    gpio.init()

    #setup the port (same as raspberry pi's gpio.setup() function)
    switch = port.PA0
    gpio.setcfg(switch, gpio.OUTPUT)

    #now we do something (light up the LED)
    gpio.output(switch, gpio.HIGH)

    #turn off the LED after 2 seconds
    sleep(0.1)
    gpio.output(switch, gpio.LOW)

if __name__ == "__main__":
    switch_status()