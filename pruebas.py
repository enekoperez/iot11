# prerequisites: pip install requests
import requests

import config

# Definimos la información de la base de datos
url = config.Config.CORLYSIS_URL
# Parametros de la base de datos de corlisys
db = config.Config.CORLYSIS_DATABASE
u = config.Config.CORLYSIS_USER
p = config.Config.CORLYSIS_PASSWORD
params = {"db": db, "u": u, "p": p}


def main():
    payload = "t3,k=v t=22.5"
    print(payload)
    r = requests.post(url, params=params, data=payload)
    print(r)


# !/usr/bin/env python

from grove.grove_ryb_led_button import GroveLedButton


def led():
    ledbtn = GroveLedButton(5)

    while True:
        ledbtn.led.light(True)
        time.sleep(1)

        ledbtn.led.light(False)
        time.sleep(1)


# !/usr/bin/env python
import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer


def buzzer2():
    # Grove - Buzzer connected to PWM port
    buzzer = upmBuzzer.Buzzer(getGpioLookup('GPIO12'))

    CHORDS = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI]
    for i in range(0, len(CHORDS)):
        buzzer.playSound(CHORDS[i], 500000)
        time.sleep(0.1)

    del buzzer
    print('application exiting...')


if __name__ == '__main__':
    led()
