# prerequisites: pip install requests
import requests

import config


class DataSender:

    # Definimos la información de la base de datos
    def __init__(self):
        # URL Corlysis
        self.url = config.Config.CORLYSIS_URL
        # Parametros de la base de datos de corlisys
        self.db = config.Config.CORLYSIS_DATABASE
        self.u = config.Config.CORLYSIS_USER
        self.p = config.Config.CORLYSIS_PASSWORD
        self.params = {"db": self.db, "u": self.u, "p": self.p}

        self.super_payload = ""
        self.n_super_payload = 0
        self.number_of_apps = config.Config.APPS

    # metodo para mandar datos a Corlysis
    def send_data(self, table_name, key, value, payload):
        payload = table_name + "," + key + "=" + value + " " + payload + "\n"

        # anade datos al payload para mandarlo a la vez
        self.super_payload += payload
        self.n_super_payload = self.n_super_payload + 1
        if self.n_super_payload == self.number_of_apps:
            r = requests.post(self.url, params=self.params, data=str(self.super_payload))
            print(r)
            self.super_payload = ""
            self.n_super_payload = 0
