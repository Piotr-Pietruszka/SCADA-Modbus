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

        self.reg_addresses = {
            "SilZawNagWst": bytearray(b'\x00\xC8'),  # 200
            "SilZawChl": bytearray(b'\x00\xCA'),  # 202
        }

        self.lineEdits_dict = {
            "SilZawNagWst": self.ui.lineEditWrite_1,
            "SilZawChl": self.ui.lineEditWrite_2,
        }

        # Push buttons
        self.ui.pushButtonSend_1.clicked.connect(lambda: self.writeFrame("SilZawNagWst"))
        self.ui.pushButtonSend_2.clicked.connect(lambda: self.writeFrame("SilZawChl"))

        # Start reading thread
        self.stop_read = False
        self.read_thread = threading.Thread(target=self.readModbus)
        self.read_thread.start()

        # Declare Instance Variables used for Modbus
        self.ModbusAddress = 0
        self.ModbusFunction = 0
        self.ModbusData = []  # Array with data. Use functions append and pop to add and remove data bytes
        self.ModbusCRC = [0, 0]
        self.ModbusDataToTransmit = []

    def writeFrame(self, element):
        """
        Write packet to serial port
        :return: None
        """
        print(f"\nSending: {element}\n")

        address = self.reg_addresses[element]
        lineEdit = self.lineEdits_dict[element]

        # Get value from editbox
        write_val_string = lineEdit.text()
        write_val_bytes = int(write_val_string).to_bytes(length=2, byteorder='big')

        ModbusData = address + write_val_bytes

        self.PreprateModbusFrame(IModbusAddr=b'\x07', IModbusFcn=b'\x06',
                                 IModbusData=ModbusData, IModbusCRC=b'\x07\x08')

        # write packet to serial port
        try:
            self.serialPort.write(b''.join(self.ModbusDataToTransmit))
        except Exception as e:
            print(str(e))
            return


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
        self.ModbusDataToTransmit.append(self.ModbusAddress)
        self.ModbusDataToTransmit.append(self.ModbusFunction)

        for byte in self.ModbusData:
            self.ModbusDataToTransmit.append(byte.to_bytes(length=1, byteorder='big'))

        self.ModbusDataToTransmit.append(self.ModbusCRC[0].to_bytes(length=1, byteorder='big'))
        self.ModbusDataToTransmit.append(self.ModbusCRC[1].to_bytes(length=1, byteorder='big'))

    def PreprateModbusFrame(self, IModbusAddr, IModbusFcn, IModbusData, IModbusCRC):
        self.ModbusAddress = IModbusAddr
        self.ModbusFunction = IModbusFcn
        self.ModbusData = IModbusData
        self.ModbusCRC = IModbusCRC
        self.encodeModbusFrame()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = ScadaApp()
    my_app.show()
    sys.exit(app.exec_())

