from services.sensores import Sensores


class MainService:

    def __init__(self):
        self.my_sensores = Sensores()
        self.execution = True

    # metodo para detener 'execute'
    def ender(self):
        self.execution = False

    # metodo main ( = execute) ejecuta el programa entero
    def main(self, request):
        conf_cerca = request['conf_distance_cerca']
        conf_lejos = request['conf_distance_lejos']
        conf_luz = request['conf_luz']
        conf_temp = request['conf_temp']
        conf_humi = request['conf_humi']

        # execute
        print('Running MainService.main...')
        self.execution = True
        while self.execution:
            self.my_sensores.distance(conf_cerca=conf_cerca, conf_lejos=conf_lejos)
            self.my_sensores.light(conf_luz=conf_luz)
            self.my_sensores.temp_and_humi(conf_temp=conf_temp, conf_humi=conf_humi)

        # para execute y reinicia valores
        if self.execution is False:
            print('Finished MainService.main...')
            self.my_sensores.lcd(message1="", message2="")
            self.my_sensores.led(state=False)
            self.my_sensores.buzz(out="distance_lejos")
