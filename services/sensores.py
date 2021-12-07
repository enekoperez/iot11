from time import sleep

import RPi.GPIO as GPIO
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT

import config
from services.data_sender import DataSender


class Sensores:

    def __init__(self):
        self.my_data_sender = DataSender()

    def led(self):  # NO FUNCIONA!!!
        print('EMPIEZA')
        GPIO.setmode(GPIO.BCM)  # Definimos BCM como nomenclatura de los pines
        led = config.Config.LED
        GPIO.setup(led, GPIO.OUT)  # Definimos el pin 24 como salida (led/buzzer)
        GPIO.output(led, GPIO.LOW)
        GPIO.output(led, GPIO.LOW)
        print('ACABA')

    def buzz(self, out):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buzzer = config.Config.BUZZER
        GPIO.setup(buzzer, GPIO.OUT)
        if out == "distance_cerca":  # high
            GPIO.output(buzzer, GPIO.HIGH)
        elif out == "distance_media":  # medium
            GPIO.output(buzzer, GPIO.HIGH)
            sleep(0.25)
            GPIO.output(buzzer, GPIO.LOW)
            sleep(0.25)
        elif out == "distance_lejos":  # low
            GPIO.output(buzzer, GPIO.LOW)

    def distance(self, conf_cerca, conf_lejos):
        # Grove - Ultrasonic Ranger connected to port D16
        sensor = GroveUltrasonicRanger(config.Config.DISTANCE)
        # while True:
        distance = sensor.get_distance()
        # print('{} cm'.format(distance))
        if distance < int(conf_cerca):
            self.buzz("distance_cerca")
        elif int(conf_cerca) < distance < int(conf_lejos):
            self.buzz("distance_media")
        elif distance > int(conf_lejos):
            self.buzz("distance_lejos")

        self.my_data_sender.send_data(table_name='distance_data', key='key', value='value',
                                      payload='distance=' + str(distance))
        return {'distance': distance}

    def light(self, conf_luz):
        # Grove - Light Sensor connected to port A0
        sensor = GroveLightSensor(config.Config.LIGHT)
        light = sensor.light

        if light > int(conf_luz):
            print('light value {}'.format(light))

        self.my_data_sender.send_data(table_name='light_data', key='key', value='value',
                                      payload='light=' + str(light))
        return {'light': light}

    def temp_and_humi(self, conf_temp, conf_humi):
        # Grove - Sensor de temperatura y humedad DTH11 conectado a la GPIO5
        sensor = DHT('11', config.Config.TEMP_AND_HUM)
        humi, temp = sensor.read()

        if temp > int(conf_temp):
            print('temp(C):', temp)
        if humi > int(conf_humi):
            print('humi(%):', humi)

        self.my_data_sender.send_data(table_name='temp_hum_data', key='key', value='value',
                                      payload='temperature=' + str(temp) + ',humidity=' + str(humi))
        return {'temp': temp, 'humi': humi}
