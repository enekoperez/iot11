# prerequisites: pip install requests
import requests

import config


class DataSender:

    def __init__(self):
        # Definimos la información de la base de datos
        self.url = config.Config.CORLYSIS_URL
        # Parametros de la base de datos de corlisys
        self.db = config.Config.CORLYSIS_DATABASE
        self.u = config.Config.CORLYSIS_USER
        self.p = config.Config.CORLYSIS_PASSWORD
        self.params = {"db": self.db, "u": self.u, "p": self.p}
        self.super_payload = ""
        self.n_super_payload = 0
        self.number_of_apps = config.Config.APPS

    def send_data(self, table_name, key, value, payload):
        payload = table_name + "," + key + "=" + value + " " + payload + "\n"

        self.super_payload += payload
        self.n_super_payload = self.n_super_payload + 1
        if self.n_super_payload == self.number_of_apps:
            r = requests.post(self.url, params=self.params, data=str(self.super_payload))
            print(r)
            self.super_payload = ""
            self.n_super_payload = 0
