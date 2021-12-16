#!/usr/bin/python
import bluetooth
import time

HectorIN = 0
HectorOUT = 0

print
"In/Out Board"

while True:
    print
    "Buscando " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
result = bluetooth.lookup_name('A0:18:28:59:XX:XX', timeout=5)
if (result != None):
    print
    "Hector: in"
if HectorIN == 0:
    HectorIN = HectorIN + 1
import subprocess

subprocess.call(['bash', '/home/pi/alarma_apaga.sh'])
subprocess.call(['bash', '/home/pi/textoAvoz.sh', 'Bienvenido a casa Hector'])
HectorOUT = 0
time.sleep(300)
else:
print
"Hector: out"
HectorIN = 0
HectorOUT = HectorOUT + 1
print
"Hector IN:"
print
HectorIN
print
"HectorOUT"
print
HectorOUT
print
"------"
