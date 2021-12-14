class Config(object):
    DEBUG = False
    TEST = False

    # GENERAL
    PORT = 3000
    APPS = 2 # 3

    # CORLYSIS
    CORLYSIS_URL = "https://corlysis.com:8086/write"
    CORLYSIS_DATABASE = "iot1"
    CORLYSIS_USER = "token"
    CORLYSIS_PASSWORD = "c18ec5995bb7cd3207d0dad8a71e2a99"

    # SENSORES
    BUZZER = 26
    DISTANCE = 16
    LIGHT = 0
    TEMP_AND_HUM = 5
    LED = 5
    # LCD = 12C
