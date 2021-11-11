import serial
import fixedint
from gui import *
import time


class ScadaApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ScadaApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serialPort = serial.Serial(port="COM5")
        self.i = 0  # Temp - to send response after reading

        # Push buttons
        self.ui.pushButtonSend.clicked.connect(self.writePacket)

    def writePacket(self):
        """
        Write packet to serial port
        :return: None
        """
        print("\n\nSending\n\n")

        # Get value from gui and convert it to fixed-size int
        packet_w_string = self.ui.lineEditWritePacket.text()
        packet_w_string = packet_w_string.replace(" ", "")  # remove spaces
        try:
            if packet_w_string[:2] == "0x":  # hex value given
                packet_w_int = fixedint.UInt32(int(packet_w_string, 16))
            else:  # decimal value given
                packet_w_int = fixedint.UInt32(packet_w_string)
        except Exception as e:
            print(str(e))
            print("Wrong value given")
            return

        # Here adding CRC, later adding header etc.

        # write packet to serial port

        packet_w_bytes = packet_w_int.to_bytes(2, 'big')  # change to bytes
        self.serialPort.write(packet_w_bytes)

    def read(self):
        while 1:
            # Wait until there is data waiting in the serial buffer
            if self.serialPort.in_waiting > 0:

                rec = self.serialPort.read()  # Read one byte
                # print(type(rec))
                print(rec)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = ScadaApp()
    my_app.show()
    sys.exit(app.exec_())

