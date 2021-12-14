# !/usr/bin/env python

import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton

import RPi.GPIO as GPIO


# from mraa import getGpioLookup
# from upm import pyupm_buzzer as upmBuzzer


def main():
    # Grove - LED Button connected to port D5
    button = GroveLedButton(5)

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


    # the rest of your code would go here

    # when your code ends, the last line before the program exits would be...
    GPIO.cleanup()
    gpio.cleanup()

    # remember, a program doesn't necessarily exit at the last line!


if __name__ == '__main__':
    main()
