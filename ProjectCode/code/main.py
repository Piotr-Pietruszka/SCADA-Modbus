import serial
import fixedint
import libscrc
from gui import *
import time
import threading

Color = {
    0: "background-color: red",
    1: "background-color: green"
}
Turn = {
    0: "OFF",
    1: "ON"
}
Sign = {
    0: "+",
    1: "-"
}


class ScadaApp(QtWidgets.QMainWindow):
    def __init__(self):
        print("!> Calling __init__")
        super(ScadaApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serialPort = serial.Serial(port="COM5",
                                        timeout=0.004,  # 4 ms
                                        inter_byte_timeout=0.002)  # 2 ms
        self.i = 0  # Temp - to send response after reading

        self.poll_id = 0
        self.poll_id_reg_addresses = { # - used to poll specific register
            0: 0x000A,      # 10
            1: 0x000E,      # 14
            2: 0x0064,      # 100
            3: 0x0065,      # 101
            4: 0x00C8,      # 200
            5: 0x00CA,      # 202
            6: 0x00D2,      # 210
            7: 0x00D3,      # 211
            8: 0x00E1,      # 225
            9: 0x012D,      # 301
            10: 0x012E,     # 302
        }

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
        self.ModbusLastRegAddressUsed = 0
        self.ModbusFunction = 0
        self.ModbusLastFunctionUsed = 0
        self.ModbusData = []  # Array with data. Use functions append and pop to add and remove data bytes
        self.ModbusCRC = []
        self.ModbusDataToTransmit = []
        self.ModbusDataReceived = []
        self.ExpectedReceiveLength = 0

        self.Register301Value = 0
        self.Register302Value = 0

        # Start polling values
        self.startUpdateThread()

    def writeFrame(self, element):
        """
        Write packet to serial port
        :return: None
        """
        print("!> Calling writeFrame")
        self.is_updating = False  # clear updating flag - stop polling registers
        time.sleep(0.004)  # 4ms wait for inter-frame silent period
        while not self.is_writing:  # wait till current register update finishes
            time.sleep(0.05)
        self.update_thread.join()

        address = self.reg_addresses[element]
        lineEdit = self.lineEdits_dict[element]

        if (("SilZawNagWst" == element) or \
            ("SilZawChl" == element) or \
            ("PrObrWentNaw" == element) or \
            ("PrObrWentWyw" == element) or \
            ("Recyrkulacja" == element)):
            # Get value from editbox
            print("!> Writing 2 bytes")
            try:
                write_val_string = lineEdit.text()
                write_val_int = round(float(write_val_string)*255.0/100.0)
                if write_val_int > 255 or write_val_int < 0:
                    raise
                write_val_bytes = write_val_int.to_bytes(length=2, byteorder='big')
            except:
                error_msg_box = QtWidgets.QMessageBox()
                error_msg_box.setWindowTitle("Error")
                error_msg_box.setText('Wrong value given')
                x = error_msg_box.exec_()
                self.startUpdateThread()
                return x
            ModbusData = address + write_val_bytes
            self.PrepareModbusFrame(IModbusAddr=b'\x07', IModbusFcn=b'\x06',
                                    IModbusData=ModbusData)
        elif (("ZalPompNagWst" == element) or \
             ("ZalWentNaw" == element) or \
             ("ZalWentWyw" == element)):
            # Get value from editbox
            print("!> Writing bit")
            try:
                write_val_string = lineEdit.text()
                # Reg 301.0 - shift=0
                if ("ZalPompNagWst" == element):
                    if (0 == int(write_val_string)):
                        write_val_int = self.Register301Value & 0b1111111111111110
                    else:
                        write_val_int = self.Register301Value | 0b0000000000000001
                # Reg 302.0 - shift=0
                elif ("ZalWentNaw" == element):
                    if (0 == int(write_val_string)):
                        write_val_int = self.Register302Value & 0b1111111111111110
                    else:
                        write_val_int = self.Register302Value | 0b0000000000000001
                # Reg 302.1 - shift=1
                elif ("ZalWentWyw" == element):
                    print("!> WRITING THEM WYW")
                    if (0 == int(write_val_string)):
                        print("!> WRITING THEM WYW 0")
                        write_val_int = self.Register302Value & 0b1111111111111100
                    else:
                        print("!> WRITING THEM WYW 1")
                        write_val_int = self.Register302Value | 0b0000000000000010
                write_val_bytes = write_val_int.to_bytes(length=2, byteorder='big')
                if (int(write_val_string) > 1):
                    raise
            except:
                error_msg_box = QtWidgets.QMessageBox()
                error_msg_box.setWindowTitle("Error")
                error_msg_box.setText('Wrong value given')
                x = error_msg_box.exec_()
                self.startUpdateThread()
                return x
            ModbusData = address + write_val_bytes
            self.PrepareModbusFrame(IModbusAddr=b'\x07', IModbusFcn=b'\x06',
                                    IModbusData=ModbusData)
        else:
            print("!> writeFrame: element error")

        self.ui.logsBrowser.append("OUT: "+' '.join([str(hex(int.from_bytes(item, "big"))) for item in self.ModbusDataToTransmit]))
        # write packet to serial port
        self.ExpectedReceiveLength = len(self.ModbusDataToTransmit)
        print("!> Writing to Port")
        try:
            self.serialPort.write(b''.join(self.ModbusDataToTransmit))
        except Exception as e:
            print(str(e))
            self.startUpdateThread()
            return

        self.ModbusDataReceived.clear()

        # Read response
        self.stop_read = False
        self.read_thread = threading.Thread(target=self.readModbus)
        self.read_thread.start()

        time.sleep(0.5)  # Wait for response before continuing update
        self.startUpdateThread()  # Keep updating

    def readCommand(self, start_address, no_regs):
        """
        Write readCommand - frame with function code = 0x03
        :param start_address: first address to read
        :param no_regs: number of registers to read
        :return:
        """
        print("!> calling readCommand")
        self.ModbusLastRegAddressUsed = start_address
        #expected amount of received data is:
        # ctrl addr + function code + amount of read bytes + 2*registers amount + CRC (2 bytes)
        self.ExpectedReceiveLength = 1 + 1 + 1 + 2*no_regs + 2
        start_address = start_address.to_bytes(length=2, byteorder='big')
        no_regs = no_regs.to_bytes(length=2, byteorder='big')
        ModbusData = start_address + no_regs
        self.PrepareModbusFrame(IModbusAddr=b'\x07', IModbusFcn=b'\x03',
                                IModbusData=ModbusData)

        # write packet to serial port
        print("!> Writing to Port")
        try:
            self.serialPort.write(b''.join(self.ModbusDataToTransmit))
        except Exception as e:
            print(str(e))
            return

        self.ModbusDataReceived.clear()
        # Read response for read command
        self.stop_read = False
        self.read_thread = threading.Thread(target=self.readModbus)
        self.read_thread.start()

    def startUpdateThread(self):
        """
        Just to wrap up starting update thread
        """
        self.is_writing = False  # reading flag cleared
        self.is_updating = True  # update flag set
        self.update_thread = threading.Thread(target=self.updateValues)  # Start updating thread
        self.update_thread.start()

    def updateValues(self):
        """
        Polling register values, to keep them up-to-date
        :return:
        """
        print("!> calling updateValues")
        while self.is_updating:
            print("updating values!")
            self.readCommand(start_address=self.poll_id_reg_addresses[self.poll_id], no_regs=2)  # write read command
            self.poll_id = (self.poll_id + 1)%11

            if not self.is_updating:  # additional exit condition - too speed writing up
                break
            time.sleep(1)
        self.is_writing = True

    def readModbus(self):
        print("!> calling readModbus")
        """
        Reading from serial port
        :return:
        """
        while not self.stop_read:
            # Wait until there is data waiting in the serial buffer (first byte comes)
            if self.serialPort.in_waiting > 0:
                # Compose packet from bytes, get value from it
                rec = self.serialPort.read(20)  # Read whole frame - inter_byte_timeout ensures single frame read
                print(f"!> received raw data: {rec}\n")
                self.ModbusDataReceived.extend([b for b in rec])
                self.stop_read = True
                self.ProcessModbusFrame()

    def closeEvent(self, event):
        print("!> calling closeEvent \n")
        """
        Added closing read thread
        """
        self.stop_read = True
        self.read_thread.join()

        self.is_updating = False
        self.update_thread.join()
        self.is_writing = True

        event.accept()

# Decode the data from rawData
    def decodeModbusFrame(self, rawData):
        print("!> calling decodeModbusFrame")
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
            print("!> Visualisation: Decode Status Error")
            self.ui.lineEditResponse.setText("CRC ERROR!")
        elif (0x86 == self.ModbusFunction):
            print("!> Visualisation: Register Read Only Error")
            self.ui.lineEditResponse.setText("REGISTER READ ONLY!")
        else:
            self.ui.lineEditResponse.setText(' '.join([str(item) for item in self.ModbusData]))
            # No match-case since using Python pre-3.10

            # code 0x03 - reading SINGLE register ( not implementing reading multiple registers )
            if (0x03 == self.ModbusFunction):
                print("!> Visualisation: code 0x03 begin")
                Address_16 = self.ModbusLastRegAddressUsed
                Value_16 = (self.ModbusData[2]<<8) | self.ModbusData[3]
            # code 0x06 - repeat response from writing )
            elif (0x06 == self.ModbusFunction):
                print("!> Visualisation: code 0x06 begin")
                # get written data address and value from response
                Address_16 = (self.ModbusData[1]<<8) | self.ModbusData[2]
                Value_16 = (self.ModbusData[3]<<8) | self.ModbusData[4]
            else:
                print("!> Visualisation: Function code error")
                self.ui.lineEditResponse.setText("FUNCTION CODE ERROR")
                return -1

            # update data in given register UI segment
            if (10 == Address_16):  # 1 Fix
                print("!> Visualisation: Setting value at register 10")
                sign = Sign[(Value_16 & 0b1000000000000000) >> 15]
                int_part = ((Value_16 & 0b0111111111100000) >> 5) if sign == "+" else ~(
                            (Value_16 & 0b0111111111100000) >> 5)
                Value_s = f"{sign}{round(int_part + (Value_16 & 0b0000000000011111)*1.0/32.0, 2)}"
                self.ui.lineEditValue_1.setText(Value_s)
                self.ui.label_f_1.setText(Value_s)
            elif (14 == Address_16):  # 2 Fix
                print("!> Visualisation: Setting value at register 14")
                sign = Sign[(Value_16 & 0b1000000000000000) >> 15]
                int_part = ((Value_16 & 0b0111111111100000) >> 5) if sign == "+" else ~(
                            (Value_16 & 0b0111111111100000) >> 5)
                Value_s = f"{sign}{round(int_part + (Value_16 & 0b0000000000011111) * 1.0 / 32.0, 2)}"
                self.ui.lineEditValue_2.setText(Value_s)
                self.ui.label_f_2.setText(Value_s)
            elif (100 == Address_16):  # 3 B
                print("!> Visualisation: Setting value at register 100.0")
                self.ui.lineEditValue_3.setText(str((Value_16 & 0b0000000000000001)>0))
                # self.ui.label_v_1.setVisible((Value_16 & 0b0000000000000001) > 0)
                self.ui.label_b_3.setText(Turn[Value_16 & 0b0000000000000001])
                self.ui.label_b_3.setStyleSheet(Color[Value_16 & 0b0000000000000001])
            elif (101 == Address_16):  # 4, 5 B
                print("!> Visualisation: Setting value at register 101.0 and 101.4")
                self.ui.lineEditValue_4.setText(str((Value_16 & 0b0000000000000001)>0))
                self.ui.label_b_4.setText(Turn[Value_16 & 0b0000000000000001])
                self.ui.label_b_4.setStyleSheet(Color[Value_16 & 0b0000000000000001])

                self.ui.lineEditValue_5.setText(str((Value_16 & 0b0000000000010000)>1))
                self.ui.label_b_5.setText(Turn[(Value_16 & 0b0000000000010000) >> 4])
                self.ui.label_b_5.setStyleSheet(Color[(Value_16 & 0b0000000000010000) >> 4])
            elif (200 == Address_16):  # 6 bj
                print("!> Visualisation: Setting value at register 200")
                self.ui.lineEditValue_6.setText(str(Value_16 * 100/255))
                self.ui.label_bj_6.setText(f"{round(Value_16*100/255, 2)}%")
            elif (202 == Address_16):  # 7 bj
                print("!> Visualisation: Setting value at register 202")
                self.ui.lineEditValue_7.setText(str(Value_16 * 100/255))
                self.ui.label_bj_7.setText(f"{round(Value_16 * 100 / 255, 2)}%")
            elif (210 == Address_16):  # 8 bj
                print("!> Visualisation: Setting value at register 210")
                self.ui.lineEditValue_8.setText(str(Value_16 * 100/255))
                self.ui.label_bj_8.setText(f"{round(Value_16 * 100 / 255, 2)}%")
            elif (211 == Address_16):  # 9 bj
                print("!> Visualisation: Setting value at register 211")
                self.ui.lineEditValue_9.setText(str(Value_16 * 100/255))
                self.ui.label_bj_9.setText(f"{round(Value_16 * 100 / 255, 2)}%")
            elif (225 == Address_16):  # 10 bj
                print("!> Visualisation: Setting value at register 225")
                self.ui.lineEditValue_10.setText(str(Value_16 * 100/255))
                self.ui.label_bj_10.setText(f"{round(Value_16 * 100 / 255, 2)}%")
            elif (301 == Address_16):  # 11 B
                self.Register301Value = Value_16
                print("!> Visualisation: Setting value at register 300.0")
                self.ui.lineEditValue_11.setText(str((Value_16 & 0b0000000000000001)>0))
                self.ui.label_b_11.setText(Turn[Value_16 & 0b0000000000000001])
                self.ui.label_b_11.setStyleSheet(Color[Value_16 & 0b0000000000000001])
            elif (302 == Address_16):  # 12, 13 B
                self.Register302Value = Value_16
                print("!> Visualisation: Setting value at register 302.0 and 302.1")
                self.ui.lineEditValue_12.setText(str((Value_16 & 0b0000000000000001)>0))
                self.ui.label_b_12.setText(Turn[Value_16 & 0b0000000000000001])
                self.ui.label_b_12.setStyleSheet(Color[Value_16 & 0b0000000000000001])

                self.ui.lineEditValue_13.setText(str((Value_16 & 0b0000000000000010)>1))
                self.ui.label_b_13.setText(Turn[(Value_16 & 0b0000000000000010) >> 1])
                self.ui.label_b_13.setStyleSheet(Color[(Value_16 & 0b0000000000000010) >> 1])

            else:
                print("!> Visualisation: Register error, received:" + str(Address_16))
                self.ui.lineEditResponse.setText("REGISTER ERROR")


if __name__ == "__main__":
    # In order to update the values in case they change.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = ScadaApp()
    my_app.show()
    sys.exit(app.exec_())

