from time import sleep

import RPi.GPIO as GPIO
from grove.display.jhd1802 import JHD1802
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ryb_led_button import GroveLedButton
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT

import config
from services.data_sender import DataSender


class Sensores:

    def __init__(self):
        self.my_data_sender = DataSender()

    # metodo led
    def led(self, state):
        # configura modo
        GPIO.setmode(GPIO.BCM)
        led = config.Config.LED  # 18
        GPIO.setup(led, GPIO.OUT)

        # enciende led si state=True
        if state is True:
            GPIO.output(led, GPIO.HIGH)
        elif state is False:
            GPIO.output(led, GPIO.LOW)

    # metodo buzzer
    def buzz(self, out):
        # configura modo
        GPIO.setmode(GPIO.BCM)
        buzzer = config.Config.BUZZER  # 26
        GPIO.setup(buzzer, GPIO.OUT)

        # distintos ritmos de sonido dependiendo de la distancia
        if out == "distance_cerca":
            GPIO.output(buzzer, GPIO.HIGH)
        elif out == "distance_media":
            GPIO.output(buzzer, GPIO.HIGH)
            sleep(0.25)
            GPIO.output(buzzer, GPIO.LOW)
            sleep(0.25)
        elif out == "distance_lejos":
            GPIO.output(buzzer, GPIO.LOW)

    # metodo lcd
    def lcd(self, message1="", message2=""):
        # configura lcd
        lcd = JHD1802()  # 12C

        # mensaje lcd superior
        lcd.setCursor(0, 0)
        lcd.write(message1)

        # mensaje lcd inferior
        lcd.setCursor(1, 0)
        lcd.write(message2)

    # metodo distancia
    def distance(self, conf_cerca=None, conf_lejos=None):
        # configura modo
        sensor = GroveUltrasonicRanger(config.Config.DISTANCE)  # 16
        distance = sensor.get_distance()

        # llama a buzzer
        if distance < int(conf_cerca):
            self.buzz(out="distance_cerca")
        elif int(conf_cerca) < distance < int(conf_lejos):
            self.buzz(out="distance_media")
        elif distance > int(conf_lejos):
            self.buzz(out="distance_lejos")

        # guarda en Corlysis
        self.my_data_sender.send_data(table_name='distance_data', key='key', value='value',
                                      payload='distance=' + str(distance))

        return {'distance': distance}

    # metodo luz
    def light(self, conf_luz=None):
        # configura modo
        sensor = GroveLightSensor(config.Config.LIGHT)  # 0
        light = sensor.light

        # enciende a apaga led
        if light > int(conf_luz):
            self.led(state=False)
        elif light < int(conf_luz):
            self.led(state=True)

        # guarda en Corlysis
        self.my_data_sender.send_data(table_name='light_data', key='key', value='value',
                                      payload='light=' + str(light))

        return {'light': light}

    # metodo para temperatura y humedad
    def temp_and_humi(self, conf_temp=None, conf_humi=None):
        # configura modo
        sensor = DHT('11', config.Config.TEMP_AND_HUM)  # 5
        humi, temp = sensor.read()

        # prepara mensaje para lcd
        message1 = 'Temperature: {}C'.format(temp)
        message2 = 'Humidity: {}%'.format(humi)

        # ensena los mensajes (si es necesario) en lcd
        if temp > int(conf_temp) and humi > int(conf_humi):
            self.lcd(message1=str(message1), message2=str(message2))
        elif temp > int(conf_temp):
            self.lcd(message1=str(message1))
        elif humi > int(conf_humi):
            self.lcd(message1=str(message2))

        # guarda en Corlysis
        self.my_data_sender.send_data(table_name='temp_hum_data', key='key', value='value',
                                      payload='temperature=' + str(temp) + ',humidity=' + str(humi))

        return {'temp': temp, 'humi': humi}
