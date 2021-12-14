# !/usr/bin/env python

import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton

import RPi.GPIO as gpio

# from mraa import getGpioLookup
# from upm import pyupm_buzzer as upmBuzzer
import config


def main():
    # Grove - LED Button connected to port D5
    button = GroveLedButton(config.Config.LED)

    # Grove - Buzzer connected to PWM port
    # buzzer = upmBuzzer.Buzzer(getGpioLookup('GPIO12'))

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            print('single click')
            button.led.light(True)
            # buzzer.playSound(upmBuzzer.BUZZER_DO, 500000)

        elif event & Button.EV_LONG_PRESS:
            print('long press')
            button.led.light(False)
            # buzzer.playSound(upmBuzzer.BUZZER_DO, 1000000)

    button.on_event = on_event

    gpio.shutdown()

    gpio.unProvisionPin(config.Config.LED)

    while True:
        try:
            # do any other processing, while waiting for the edge detection
            time.sleep(1)  # sleep 1 sec
        finally:
            gpio.cleanup()


if __name__ == '__main__':
    main()
