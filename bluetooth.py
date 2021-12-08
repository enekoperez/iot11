# simple inquiry example
import bluetooth


def main():
    # Bluetooth stuff
    bd_addr = "88:46:04:59:ae:37"
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    # 0x1X for straight forward and 0x11 for very slow to 0x1F for fastest
    sock.send("\x1A")


if __name__ == '__main__':
    main()
