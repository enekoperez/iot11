# !/usr/bin/env python

import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton


# from mraa import getGpioLookup
# from upm import pyupm_buzzer as upmBuzzer
import config


def main():
    # Grove - LED Button connected to port D5
    button = GroveLedButton(config.Config.LED)

    # Grove - Buzzer connected to PWM port
    # buzzer = upmBuzzer.Buzzer(getGpioLookup('GPIO12'))

    button.led.light(True)
            # buzzer.playSound(upmBuzzer.BUZZER_DO, 500000)


if __name__ == '__main__':
    main()
