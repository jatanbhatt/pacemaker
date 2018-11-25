import serial
import time
import struct
import sys

#Testing Serial Communication

#for mac:
#   plug in device
#   in terminal run: ls /dev/tty.usb*
#   copy the valuaes after "usbmodem" and replace ___ with them
ser = serial.Serial(
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    port = "/dev/tty.usbmodem14101",
    baudrate=115200
)

#for windows:
#   When plugging in device note with COM port it is, can also be found in computer settings
#   copy the values after "COM" and replace ___ with them

# ser = serial.Serial(
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     port = "COM_",
#     baudrate=115200


#print("Opening Serial Port")
#ser.open()                         #use if for some reason serial port is not already opened
print("Is Serial Port Open:",ser.isOpen())

#setting up manual bytestream (115 bytes)

list = [16]                         #Start byte, remove if required
list.append(11)                     #Setting parameters mode
list.extend([0,0,0,0,0,0,0,120])    #p_URL
list.extend([0,0,0,0,0,0,0,60])     #p_LRL
list.extend([0,0,0,0,0,0,0,35])     #aPulseAmplitude (you have to divide by 10 on your end)
list.extend([0,0,0,0,0,0,0,35])     #vPulseAmplitude (you have to divide by 10 on your end)
list.extend([0,0,0,0,0,0,0,40])     #aPulseWidth (you have to divide by 10 on your end)
list.extend([0,0,0,0,0,0,0,40])     #vPulseWidth (you have to divide by 10 on your end)
list.append(0)                      #VOO Mode
list.extend([0,0,0,0,0,0,0,0])      #p_VRP
list.extend([0,0,0,0,0,0,0,0])      #p_ARP
list.extend([0,0,0,0,0,0,0,0])      #p_Hysteris
list.extend([0,0,0,0,0,0,0,0])      #p_responseFactor
list.extend([0,0,0,0,0,0,0,0])      #p_MSR
list.extend([0,0,0,0,0,0,0,0])      #p_activityThreshold
list.extend([0,0,0,0,0,0,0,0])      #p_reactionTime
list.extend([0,0,0,0,0,0,0,0])      #p_recoveryTime

#print(list)
to_send = bytes(list)
#print(to_send)

ser.write(to_send)
print ("Number of Bytes sent:",ser.write(to_send))

#print (ser.read(115))
#print (ser.name)

#print("Closing Serial Port")
ser.close()
print("Serial Port Closed")
