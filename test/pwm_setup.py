import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
)


def writeByte(number):
        
        byte = number.to_bytes(1, "big")
        
        
        print(byte)

if __name__ == "__main__":
    while True:
       test = ser.write(bytes(input("input pwm: "), "utf-8"))