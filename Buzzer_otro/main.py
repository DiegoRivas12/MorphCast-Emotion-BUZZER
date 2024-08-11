import serial
import time

arduino = serial.Serial(port='COM4',  baudrate=9600, timeout=.1)
if not arduino.is_open:
   arduino.open()

def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data



num = input("Enter a number: ")
value  = write_read(num)
#print(value)

if arduino.is_open:
   arduino.close()