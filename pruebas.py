# prerequisites: pip install requests
import requests

import config

# Definimos la información de la base de datos
url = config.Config.CORLYSIS_URL
# Parametros de la base de datos de corlisys
db = config.Config.CORLYSIS_DATABASE
u = config.Config.CORLYSIS_USER
p = config.Config.CORLYSIS_PASSWORD
params = {"db": db, "u": u, "p": p}


def main():
    print(1)

    payload = "t3,k=v t=22.5"
    print(payload)
    r = requests.post(url, params=params, data=payload)
    print(r)


if __name__ == '__main__':
    main()
