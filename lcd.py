#!/usr/bin/env python

import time

from grove.display.jhd1802 import JHD1802


def main():
    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    lcd.setCursor(1, 0)
    lcd.write('7 cristiano ronaldo 7')

    print('application exiting...')


if __name__ == '__main__':
    main()