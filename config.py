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
    CORLYSIS_PASSWORD = "53981e81e03856e12b8f7d109a27eda1"

    # SENSORES
    BUZZER = 26
    DISTANCE = 16
    LIGHT = 0
    TEMP_AND_HUM = 5
    LED = 18
    # LCD = I2C
