import serial
import fixedint


serialPort = serial.Serial(port="COM5")

i = 0  # Temp - to send response after reading


while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        rec = serialPort.read()  # Read one byte
        # print(type(rec))
        print(rec)

        i+=1
        if i > 7:
            # Send respones
            print("\n\nSending\n\n")
            x = fixedint.UInt32(0x80FF)
            response = x.to_bytes(2, 'big')
            serialPort.write(response)
            i = 0



