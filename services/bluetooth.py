import subprocess


class Bluetooth:

    def running_commands(self):
        subprocess.run('/iot11/bt.sh')

    running_commands()
