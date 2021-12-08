from services.sensores import Sensores


class MainService:

    def __init__(self):
        self.my_sensores = Sensores()
        self.execution = True

    def ender(self):
        self.execution = False

    def main(self, request):  # DUDA, ¿ se podra poner aqui =None ?
        conf_cerca = request['conf_distance_cerca']
        conf_lejos = request['conf_distance_lejos']
        conf_luz = request['conf_luz']
        conf_temp = request['conf_temp']
        conf_humi = request['conf_humi']

        print('Running MainService.main ...')
        while self.execution:
            # sensores.led()
            self.my_sensores.distance(conf_cerca=conf_cerca, conf_lejos=conf_lejos)
            self.my_sensores.light(conf_luz=conf_luz)
            self.my_sensores.temp_and_humi(conf_temp=conf_temp, conf_humi=conf_humi)

        if self.execution is False:
            print('Finished MainService.main ...')
