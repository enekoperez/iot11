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


def send_b(received_data):
    received_data = str(received_data)
    to_send_data = received_data.encode('utf-8')
    ser = serial.Serial('/dev/rfcomm0')
    ser.isOpen()
    ser.write(to_send_data)




