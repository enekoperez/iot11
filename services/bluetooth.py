import subprocess
from time import sleep

import serial


def running_commands():
    pro = subprocess.run('sudo rfcomm watch hci0')
    print(pro.returncode)
    if int(pro.returncode) == 0:
        print("pass")
    else:
        print("fail")


def send_b(data):
    data = str(data)
    b = bytes(data, 'utf-8')
    ser = serial.Serial('/dev/rfcomm0')
    ser.isOpen()
    ser.write(b)




