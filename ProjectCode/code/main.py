import serial
import fixedint
import libscrc
from gui import *
import time
import threading


class ScadaApp(QtWidgets.QMainWindow):
    def __init__(self):
        print("!> Calling __init__")
        super(ScadaApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serialPort = serial.Serial(port="COM5")
        self.i = 0  # Temp - to send response after reading

        self.reg_addresses = { # - register adresses  of non-binary outputs to set
            "SilZawNagWst": bytearray(b'\x00\xC8'),     # 200
            "SilZawChl": bytearray(b'\x00\xCA'),        # 202
            "PrObrWentNaw": bytearray(b'\x00\xD2'),     # 210
            "PrObrWentWyw": bytearray(b'\x00\xD3'),     # 211
            "Recyrkulacja": bytearray(b'\x00\xE1'),     # 225
            "ZalPompNagWst": bytearray(b'\x01\x2D'),    # 301.0
            "ZalWentNaw": bytearray(b'\x01\x2E'),       # 302.0
            "ZalWentWyw": bytearray(b'\x01\x2E'),       # 302.1
        }


        self.lineEdits_dict = { # GUI lineEditWrite IDs
            "SilZawNagWst": self.ui.lineEditWrite_1,
            "SilZawChl": self.ui.lineEditWrite_2,
            "PrObrWentNaw": self.ui.lineEditWrite_3,
            "PrObrWentWyw": self.ui.lineEditWrite_4,
            "Recyrkulacja": self.ui.lineEditWrite_5,
            "ZalPompNagWst": self.ui.lineEditWrite_6,
            "ZalWentNaw": self.ui.lineEditWrite_7,
            "ZalWentWyw": self.ui.lineEditWrite_8,
        }

        # Push buttons events
        self.ui.pushButtonSend_1.clicked.connect(lambda: self.writeFrame("SilZawNagWst"))
        self.ui.pushButtonSend_2.clicked.connect(lambda: self.writeFrame("SilZawChl"))
        self.ui.pushButtonSend_3.clicked.connect(lambda: self.writeFrame("PrObrWentNaw"))
        self.ui.pushButtonSend_4.clicked.connect(lambda: self.writeFrame("PrObrWentWyw"))
        self.ui.pushButtonSend_5.clicked.connect(lambda: self.writeFrame("Recyrkulacja"))
        self.ui.pushButtonSend_6.clicked.connect(lambda: self.writeFrame("ZalPompNagWst"))
        self.ui.pushButtonSend_7.clicked.connect(lambda: self.writeFrame("ZalWentNaw"))
        self.ui.pushButtonSend_8.clicked.connect(lambda: self.writeFrame("ZalWentWyw"))

        # Declare Instance Variables used for Modbus
        self.ModbusAddress = 0
        self.ModbusLastAddressUsed = 0
        self.ModbusFunction = 0
        self.ModbusLastFunctionUsed = 0
        self.ModbusData = []  # Array with data. Use functions append and pop to add and remove data bytes
        self.ModbusCRC = []
        self.ModbusDataToTransmit = []
        self.ModbusDataReceived = []
        self.ExpectedReceiveLength = 0

    def writeFrame(self, element):
        print("!> Calling writeFrame \n")
        """
        Write packet to serial port
        :return: None
        """
        #print(f"Sending: {element}")

        address = self.reg_addresses[element]
        lineEdit = self.lineEdits_dict[element]

        # Get value from editbox
        try:
            write_val_string = lineEdit.text()
            write_val_bytes = int(write_val_string).to_bytes(length=2, byteorder='big')
            if int(write_val_string) > 255:
                raise
        except:
            error_msg_box = QtWidgets.QMessageBox()
            error_msg_box.setWindowTitle("Error")
            error_msg_box.setText('Wrong value given')
            x = error_msg_box.exec_()
            return x

        ModbusData = address + write_val_bytes

        # TODO: run PrepareModbusFrame with different arguments depending on what button was pressed
        # (Binary outputs require different operations)
        self.PrepareModbusFrame(IModbusAddr=b'\x07', IModbusFcn=b'\x06',
                                 IModbusData=ModbusData)

        self.ui.logsBrowser.append("OUT: "+' '.join([str(hex(int.from_bytes(item, "big"))) for item in self.ModbusDataToTransmit]))
        # write packet to serial port
        self.ExpectedReceiveLength = len(self.ModbusDataToTransmit)
        print("!> Writing to Port")
        try:
            self.serialPort.write(b''.join(self.ModbusDataToTransmit))
        except Exception as e:
            print(str(e))
            return

        self.ModbusDataReceived.clear()

        # Start reading thread
        self.stop_read = False
        self.read_thread = threading.Thread(target=self.readModbus)
        self.read_thread.start()


    def readModbus(self):
        print("!> calling readModbus")
        """
        Reading from serial port
        :return:
        """

        while not self.stop_read:
            # Wait until there is data waiting in the serial buffer
            if self.serialPort.in_waiting > 0:

                # Compose packet from bytes, get value from it
                rec = self.serialPort.read()  # Read one byte

                #rec_int = fixedint.UInt32.from_bytes(rec)
                rec_int = int.from_bytes(rec, "big")
                self.ui.lineEditResponse.setText("{:x}".format(rec_int))
                # print(type(rec))
                # print(rec_int)
                self.ModbusDataReceived.append(rec_int)

            if (self.ExpectedReceiveLength == len(self.ModbusDataReceived)):
                self.stop_read = True
                self.ProcessModbusFrame()

    def closeEvent(self, event):
        print("!> calling closeEvent \n")
        """
        Added closing read thread
        """
        self.stop_read = True
        self.read_thread.join()
        event.accept()

# Decode the data from rawData
    def decodeModbusFrame(self, rawData):
        print("!> calling decodeModbusFrame, Data: ")
        print(rawData)
        print("Data length:")
        print(len(rawData))
        # Check if CRC is correct
        byte1 = rawData[len(rawData) - 2]
        byte1 = rawData[len(rawData) - 1]
        self.ModbusCRC = [rawData[len(rawData) - 2], rawData[len(rawData) - 1]]
        rawData.pop(len(rawData) - 1)
        rawData.pop(len(rawData) - 1)
        ModbusCRC_16 = (self.ModbusCRC[1]<<8) | self.ModbusCRC[0]
        tempRawData = []
        for byte in rawData:
            tempRawData.append(byte.to_bytes(length=1, byteorder='big'))
        CalculatedCRC_16 = (libscrc.modbus(b''.join(tempRawData))).to_bytes(length=2, byteorder='little')
        tempCalculatedCRC_16 = [CalculatedCRC_16[0], CalculatedCRC_16[1]]
        CalculatedCRC_16 = (tempCalculatedCRC_16[1]<<8) | tempCalculatedCRC_16[0]
        if (CalculatedCRC_16 != ModbusCRC_16):
            return -1

        self.ModbusAddress = rawData[0]
        rawData.pop(0)
        self.ModbusFunction = rawData[0]
        
        i = 0
        self.ModbusData = []
        for byte in rawData:
            self.ModbusData.append(byte)
            i = i+1
        self.ModbusFunction = self.ModbusData[0]

        return 1

# Encode the data into self.ModbusDataToTransmit
    def encodeModbusFrame(self):
        print("!> calling encodeModbusFrame")
        self.ModbusDataToTransmit.clear()
        self.ModbusDataToTransmit.append(self.ModbusAddress)
        self.ModbusDataToTransmit.append(self.ModbusFunction)

        for byte in self.ModbusData:
            self.ModbusDataToTransmit.append(byte.to_bytes(length=1, byteorder='big'))
        #remove 'b\n'
        # self.ModbusDataToTransmit.pop(len(self.ModbusDataToTransmit) - 1)

        #print("Calculating CRC from:")
        #print(self.ModbusDataToTransmit)
        self.ModbusCRC = (libscrc.modbus(b''.join(self.ModbusDataToTransmit))).to_bytes(length=2, byteorder='little')

        self.ModbusDataToTransmit.append(self.ModbusCRC[0].to_bytes(length=1, byteorder='big'))
        self.ModbusDataToTransmit.append(self.ModbusCRC[1].to_bytes(length=1, byteorder='big'))
        #print("Finished Encoding")

    def PrepareModbusFrame(self, IModbusAddr, IModbusFcn, IModbusData):
        print("!> calling PreprateModbusFrame")
        self.ModbusAddress = IModbusAddr
        self.ModbusLastAddressUsed = IModbusAddr
        self.ModbusFunction = IModbusFcn
        self.ModbusLastFunctionUsed = IModbusFcn
        self.ModbusData = IModbusData
        self.encodeModbusFrame()

# Process frame - only when frame if fully received!
    def ProcessModbusFrame(self):
        print("!> calling ProcessModbusFrame")
        self.ui.logsBrowser.append("IN:    "+' '.join([str(hex(item)) for item in self.ModbusDataReceived]))
        decodeStatus = self.decodeModbusFrame(self.ModbusDataReceived)
        
        #Check if decoded properly!
        if (-1 == decodeStatus):
            self.ui.lineEditResponse.setText("CRC ERROR!")
        elif (0x86 == self.ModbusFunction):
            self.ui.lineEditResponse.setText("REGISTER READ ONLY!")
        else:
            self.ui.lineEditResponse.setText(' '.join([str(item) for item in self.ModbusData]))
            # No match-case since using Python pre-3.10

            # code 0x07 - reading SINGLE register ( not implementing reading multiple registers )
            if (0x07 == self.ModbusFunction):
                Address_16 = self.ModbusLastAddressUsed
                Value_16 = (self.ModbusData[2]<<8) | self.ModbusData[3]
            # code 0x06 - repeat response from writing )
            elif (0x06 == self.ModbusFunction):
                # get written data address and value from response
                Address_16 = (self.ModbusData[1]<<8) | self.ModbusData[2]
                Value_16 = (self.ModbusData[3]<<8) | self.ModbusData[4]
            else:
                self.ui.lineEditResponse.setText("FUNCTION CODE ERROR")

if __name__ == "__main__":
    # TODO: Make flag "is_writing", and if that flag it not set and 'stop_read' is set, start cyclic reading of needed registers.
    # In order to update the values in case they change.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = ScadaApp()
    my_app.show()
    sys.exit(app.exec_())

