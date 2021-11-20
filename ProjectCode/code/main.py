import serial
import fixedint
import libscrc
from gui import *
import time
import threading


class ScadaApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ScadaApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serialPort = serial.Serial(port="COM5")
        self.i = 0  # Temp - to send response after reading

        # Push buttons
        self.ui.pushButtonSend.clicked.connect(self.writePacket)

        # Start reading thread
        self.stop_read = False
        self.read_thread = threading.Thread(target=self.readModbus)
        self.read_thread.start()

        # Declare Instance Variables used for Modbus
        self.ModbusAddress = 0
        self.ModbusFunction = 0
        self.ModbusData = [0] #Array with data. Use functions append and pop to add and remove data bytes
        self.ModbusCRC = [0, 0]
        self.ModbusDataToTransmit = [0]

    def writePacket(self):
        """
        Write packet to serial port
        :return: None
        """
        print("\nSending\n")

        # if packet_w_string[:2] == "0x":  # hex value given
        # packet_w_int = fixedint.UInt32(int(packet_w_string, 16))
        # packet_w_int = fixedint.UInt32(packet_w_string)

        # Get hex value from editbox - to be changed to creating packet from stored values
        packet_w_string = self.ui.lineEditWritePacket.text()
        packet_w_string = packet_w_string.replace(" ", "")  # remove spaces
        try:
            packet_w_bytes = bytearray.fromhex(packet_w_string)
        except Exception as e:
            print(str(e))
            print("Wrong value given")
            return

        # Here (or above try-catch) adding CRC, adding header etc.

        # write packet to serial port
        self.serialPort.write(packet_w_bytes)

    def readModbus(self):
        """
        Reading from serial port
        :return:
        """
        while not self.stop_read:
            # Wait until there is data waiting in the serial buffer
            if self.serialPort.in_waiting > 0:

                # Compose packet from bytes, get value from it
                rec = self.serialPort.read()  # Read one byte

                rec_int = fixedint.UInt32.from_bytes(rec)
                self.ui.lineEditResponse.setText("{:x}".format(rec_int))
                # print(type(rec))
                print(rec_int)

    def closeEvent(self, event):
        """
        Added closing read thread
        """
        self.stop_read = True
        self.read_thread.join()
        event.accept()

# Decode the data from rawData
    def decodeModbusFrame(self, rawData):
        # Check if CRC is correct
        self.ModbusCRC[0] = rawData[len(rawData) - 2]
        self.ModbusCRC[1] = rawData[len(rawData) - 1]
        rawData.pop(len(rawData) - 1)
        rawData.pop(len(rawData) - 1)
        ModbusCRC_16 = (self.ModbusCRC[1]<<8) | self.ModbusCRC[0]
        CalculatedCRC_16 = libscrc.modbus(self.ModbusCRC)
        if (CalculatedCRC_16 != ModbusCRC_16):
            return -1
        
        
        self.ModbusAddress = rawData[0]
        rawData.pop(0)
        self.ModbusFunction = rawData[0]
        
        i = 0
        for byte in rawData:
            self.ModbusData[i] = byte
            i = i+1
        return 1

# Encode the data into self.ModbusDataToTransmit
    def encodeModbusFrame(self):
        self.ModbusDataToTransmit.clear()
        self.ModbusDataToTransmit[0] = self.ModbusAddress
        self.ModbusDataToTransmit[1] = self.ModbusFunction
        i = 2
        
        for byte in self.ModbusData:
            self.ModbusDataToTransmit[i] = byte
            i = i + 1
        self.ModbusDataToTransmit[i] = self.ModbusCRC[0]
        i = i + 1
        self.ModbusDataToTransmit[i] = self.ModbusCRC[1]

    def PreprateModbusFrame(self, IModbusAddr, IModbusFcn, IModbusData, IModbusCRC):
        self.ModbusAddress = IModbusAddr
        self.ModbusFunction = IModbusFcn
        self.ModbusData = IModbusData
        self.ModbusCRC = IModbusCRC
        self.encodeModbusFrame();

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = ScadaApp()
    my_app.show()
    sys.exit(app.exec_())

