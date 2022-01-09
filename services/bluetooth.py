import subprocess
from time import sleep

import serial


def running_commands():
    pro = subprocess.run('/home/pi/iot11/bt.sh')
    print(pro.returncode)
    if int(pro.returncode) == 0:
        print("pass")
    else:
        print("fail")


# running_commands()
#sleep(10)

data = str(0)
b = bytes(data, 'utf-8')
ser = serial.Serial('/dev/rfcomm0')
ser.isOpen()
ser.write(b)
