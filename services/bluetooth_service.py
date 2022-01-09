import serial


class BluetoothService:

    def send_b(self, received_data):
        received_data = str(received_data + '\r\n')
        to_send_data = received_data.encode('utf-8')
        ser = serial.Serial('/dev/rfcomm0')
        ser.isOpen()
        ser.write(to_send_data)
