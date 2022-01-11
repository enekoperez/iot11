class Config(object):
    DEBUG = False
    TEST = False

    # GENERAL
    PORT = 3000
    APPS = 3

    # CORLYSIS
    CORLYSIS_URL = "https://corlysis.com:8086/write"
    CORLYSIS_DATABASE = "iot1"
    CORLYSIS_USER = "token"
    CORLYSIS_PASSWORD = "a00797325b77d4c7be48a932b2172177"

    # SENSORES
    BUZZER = 26
    DISTANCE = 16
    LIGHT = 0
    TEMP_AND_HUM = 5
    LED = 18
    # LCD = I2C
