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

    def led(self, state):
        ledbtn = GroveLedButton(config.Config.LED)

        if state is True:
            ledbtn.led.light(True)
        elif state is False:
            ledbtn.led.light(False)

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

    def lcd(self, message1="", message2=""):
        # Grove - 16x2 LCD(White on Blue) connected to I2C port
        lcd = JHD1802()

        lcd.setCursor(0, 0)
        lcd.write(message1)

        lcd.setCursor(1, 0)
        lcd.write(message2)

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
            message = 'Light value {}'.format(light)
            # self.lcd(message1=str(message))
            self.led(state=False)
        elif light < int(conf_luz):
            self.led(state=True)

        self.my_data_sender.send_data(table_name='light_data', key='key', value='value',
                                      payload='light=' + str(light))
        return {'light': light}

    def temp_and_humi(self, conf_temp, conf_humi):
        # Grove - Sensor de temperatura y humedad DTH11 conectado a la GPIO5
        sensor = DHT('11', config.Config.TEMP_AND_HUM)
        humi, temp = sensor.read()

        message1 = 'Temperature: {}C'.format(temp)
        message2 = 'Humidity: {}%'.format(humi)

        if temp > int(conf_temp) and humi > int(conf_humi):
            self.lcd(message1=str(message1), message2=str(message2))
        elif temp > int(conf_temp):
            self.lcd(message1=str(message1))
        elif humi > int(conf_humi):
            self.lcd(message1=str(message2))

        self.my_data_sender.send_data(table_name='temp_hum_data', key='key', value='value',
                                      payload='temperature=' + str(temp) + ',humidity=' + str(humi))
        return {'temp': temp, 'humi': humi}
