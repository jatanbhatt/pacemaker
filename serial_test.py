import serial
import time

#Testing Serial Communication with Arduino
#ls /dev/tty.usb
ser = serial.Serial()
ser.port = "/dev/tty.usbmodem000621000000"
ser.baudrate = 115200
#ser.timeout = None

#print("Opening Serial Port")
ser.open()
print("Serial Port Opened")

#to_send = bytearray([0,16,10])

to_send = bytearray([0,1])
#to_send.append(b'1')
to_send1 = [0,16,10]
to_send2 = [0,16,11]

#hile (!ser.available)
while 1: ser.write(to_send)
print ("Number of Bytes sent:",ser.write(to_send))

    #ser.write(to_send2)
    #print ("Number of Bytes sent:",ser.write(to_send2))
    #time.sleep(.1)

#print ("Number of Bytes sent:",ser.write(to_send1))
#print (ser.read())
#print (ser.name)

#print("Closing Serial Port")
#ser.close()
#print("Serial Port Closed")
