# mateo
print("Mathew was here.")
# fishlog init
import sys
import datetime
from time import sleep
import threading
import time
from multiprocessing import Process
import statistics
import serial

class Color(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'
    # add bold variants
    RED_BOLD = '\033[1;31m'
    GREEN_BOLD = '\033[1;32m'
    YELLOW_BOLD = '\033[1;33m'
    BLUE_BOLD = '\033[1;34m'
    MAGENTA_BOLD = '\033[1;35m'
    CYAN_BOLD = '\033[1;36m'
    WHITE_BOLD = '\033[1;37m'
    END_BOLD = '\033[1;0m'
    # rainbow gradient
    RED_RAINBOW = '\033[38;5;9m'
    GREEN_RAINBOW = '\033[38;5;10m'
    # gradient between pink and blue
    PINK_BLUE = '\033[38;5;13m'




class fishlog(object):
    def __init__(self, filename="fishlog.log"):

        self.terminal = sys.stdout
        self.log = open(filename, "a")
         # write the time the file was opened
        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        time = str(time)
        sleep(1)
        self.log.write( "\n"+ f"[{time}] : " + "\n")
        # print ok into the file once it opens
        self.write(Color.GREEN_RAINBOW + """
        
   ___              __       ___                       
 /'___\ __         /\ \     /\_ \                               
/\ \__//\_\    ____\ \ \___ \//\ \     ___      __     
\ \ ,__\/\ \  /',__\\ \  _ `\ \ \ \   / __`\  /'_ `\   
 \ \ \_/\ \ \/\__, `\\ \ \ \ \ \_\ \_/\ \L\ \/\ \L\ \  
  \ \_\  \ \_\/\____/ \ \_\ \_\/\____\ \____/\ \____ \ 
   \/_/   \/_/\/___/   \/_/\/_/\/____/\/___/  \/___L\ :
                                                /\____/
                                                \_/__/ v. 2.0 by @Skipper_
        """ + Color.END)
        


        self.write(Color.CYAN_BOLD + """
                    /`·.¸
                    /¸...¸`:·
                ¸.·´  ¸   `·.¸.·´)
                : © ):´;      ¸  {
                `·.¸ `·  ¸.·´\`·¸)
                    `\\´´\¸.·´

""" + Color.END)
        sleep(1)
        self.write(Color.MAGENTA + """
[INFO] Fishlog initialized.\n""" + Color.END)
        sleep(1)
        self.write(Color.YELLOW + """
[INFO] Starting main event...\n""" + Color.END)
        sleep(1)
        self.write(Color.BLUE + """
[INFO]  Main event started.\n\n\n""" + Color.END)
                                                                

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here. 
        # ^ Thanks Copilot for the tip :P
        pass
# create a class that logs the terminal output to a file
class fishlog_logerr(object):
    def __init__(self, filename="fishlog.logerr.log"):
        self.terminal = sys.stderr
        self.log = open(filename, "a")
         # write the time the file was opened
        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        time = str(time)
        sleep(1)
        self.log.write( "\n"+ f"[{time}] : " + "\n")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

# kira init
print(Color.RED_BOLD + """
Initializing 
      ___                       ___           ___              
     /\__\          ___        /\  \         /\  \             
    /:/  /         /\  \      /::\  \       /::\  \            
   /:/__/          \:\  \    /:/\:\  \     /:/\:\  \           
  /::\__\____      /::\__\  /::\~\:\  \   /::\~\:\  \          
 /:/\:::::\__\  __/:/\/__/ /:/\:\ \:\__\ /:/\:\ \:\__\         
 \/_|:|~~|~    /\/:/  /    \/_|::\/:/  / \/__\:\/:/  /         
    |:|  |     \::/__/        |:|::/  /       \::/  /          
    |:|  |      \:\__\        |:|\/__/        /:/  /           
    |:|  |       \/__/        |:|  |         /:/  /            
     \|__|                     \|__|         \/__/             


""" + Color.END)
#libs
from colorama import Fore
import RPi.GPIO as GPIO
import socket
import sys
#----------------------------------------------------------------
# socket server? 

# servo setup
#----------------------------------------------------------------
OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
servoPin = 12                       # GPIO18 (Can connect servo pin to: 7, 11, 12, 13, 15, 16, 18, 22)
# !Attention! change 18th pin 

def map(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup_servo():
    global p
    GPIO.setmode(GPIO.BOARD)         # Numbers GPIOs by physical location
    GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin's mode to: is output
    GPIO.output(servoPin, GPIO.LOW)  # Set servoPin to low

    p = GPIO.PWM(servoPin, 50)     # set Frequece to 50Hz
    p.start(0)                     # Duty Cycle = 0
    
def servoWrite(angle):      # make the servo rotate to specific angle (0-180 degrees) 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))#map the angle to duty cycle and output it

    
def servoWriteWbackPulse(angle):
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))#map the angle to duty cycle and output it
    sleep(0.1)
    if angle == 0:
        servoWrite(70)
    elif angle == 180:
        servoWrite(70)

def loop_servo():
    while True:
        for dc in range(0, 181, 1):   #make servo rotate from 0 to 180 deg
            servoWrite(dc)     # Write to servo
            time.sleep(0.001)
        time.sleep(0.5)
        for dc in range(180, -1, -1): #make servo rotate from 180 to 0 deg
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)

#-----------------------------------------------------
"""""
# new servo setup idk 
def setup_servo2():
    global servo
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)

    servo = GPIO.PWN(11, 50)    # pin 11, 50hz
    servo.start(0)              # leerlauf

def servo2Write(angle):
    try: 

        while True:
            servo.ChangeDutyCycle(2+(angle/18))
            sleep(0.5)
            return servo.ChangeDutyCycle(0)
    finally:
        servo.stop()
        GPIO.cleanup()

"""""
# ----------------------------------------------------
# left infrared sensor
# left sensor

trigPin_left = 16
echoPin_left = 18
MAX_DISTANCE_left = 220          #define the maximum measured distance
timeOut_left = MAX_DISTANCE_left*60   #calculate timeout according to the maximum measured distance

def pulseIn_left(pin_left,level_left,timeOut_left): # function pulseIn: obtain pulse time of a pin
    t0_left = time.time()
    while(GPIO.input(pin_left) != level_left):
        if((time.time() - t0_left) > timeOut_left*0.000001):
            return 0;
    t0_left = time.time()
    while(GPIO.input(pin_left) == level_left):
        if((time.time() - t0_left) > timeOut_left*0.000001):
            return 0;
    pulseTime_left = (time.time() - t0_left)*1000000
    return pulseTime_left
    
def getSonar_left():     #get the measurement results of ultrasonic module, with unit: cm
    GPIO.output(trigPin_left,GPIO.HIGH)      #make trigPin send 10us high level 
    time.sleep(0.00001)     #10us (trigger input signal)
    GPIO.output(trigPin_left,GPIO.LOW)
    pingTime_left = pulseIn_left(echoPin_left,GPIO.HIGH,timeOut_left)   #read plus time of echoPin
    distance_left = pingTime_left * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, and calculate distance
    return distance_left
    
def setup_left():
    print (Fore.GREEN + "[INFO] UR sensor LEFT start. "+ Fore.WHITE)
    GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
    GPIO.setup(trigPin_left, GPIO.OUT)   #
    GPIO.setup(echoPin_left, GPIO.IN)    #

# create a array of distance_left with the last 10 numbers
array_left_UR = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]


def loop_left():

    newValue_left = getSonar_left()

    array_left_UR.pop()
    array_left_UR.insert(0, newValue_left)

    distance_left = statistics.mean(array_left_UR)


    if int(distance_left) <= 20:
        
        servoWriteWbackPulse(0) # rotate the servo by 20 degrees 
        #servoWrite(90)
        #servoWrite(-20) # rotate the servo back to original position 
        #!ATTENTION: check if this works. 
        print(Fore.BLUE + "Object detected LEFT, turning RIGHT." + Fore.WHITE + str(distance_left))
        

    else:
        print("UR L:: The distance is : %.2f cm"%(distance_left))

# right sensor

trigPin_right = 36
echoPin_right = 38
MAX_DISTANCE_right = 220          #define the maximum measured distance
timeOut_right = MAX_DISTANCE_right*60   #calculate timeout according to the maximum measured distance

def pulseIn_right(pin_right,level_right,timeOut_right): # function pulseIn: obtain pulse time of a pin
    t0_right = time.time()
    while(GPIO.input(pin_right) != level_right):
        if((time.time() - t0_right) > timeOut_right*0.000001):
            return 0;
    t0_right = time.time()
    while(GPIO.input(pin_right) == level_right):
        if((time.time() - t0_right) > timeOut_right*0.000001):
            return 0;
    pulseTime_right = (time.time() - t0_right)*1000000
    return pulseTime_right
    
def getSonar_right():     #get the measurement results of ultrasonic module, with unit: cm
    GPIO.output(trigPin_right,GPIO.HIGH)      #make trigPin send 10us high level 
    time.sleep(0.00001)     #10us (trigger input signal)
    GPIO.output(trigPin_right,GPIO.LOW)
    pingTime_right = pulseIn_right(echoPin_right,GPIO.HIGH,timeOut_right)   #read plus time of echoPin
    distance_right = pingTime_right * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, and calculate distance
    return distance_right
    
def setup_right():
    print (Fore.GREEN + "[INFO] UR sensor RIGHT start." + Fore.WHITE)
    GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
    GPIO.setup(trigPin_right, GPIO.OUT)   #
    GPIO.setup(echoPin_right, GPIO.IN)    #


array_right_UR = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]


def loop_right():

        newValue_right = getSonar_right()

        array_right_UR.pop()
        array_right_UR.insert(0, newValue_right)

        distance_right = statistics.mean(array_right_UR)
            # print ("UR L:: The distance is : %.2f cm"%(distance_left))

        if int(distance_right) <= 20:
            servoWriteWbackPulse(180) # rotate the servo by 20 degrees
            print(Fore.BLUE + "Object detected RIGHT, turning LEFT." + Fore.WHITE + str(distance_right))

            #time.sleep(1) # wait for one second, then rotate servo back to 0 degrees
            #!ATTENTION: check if this works.
           
                
        else:
            print("UR R:: The distance is : %.2f cm"%(distance_right))

#----------------------------------------------------------------


# pwm Motor setup 

GPIO.setmode(GPIO.BOARD)
###
# General Info: With the usage of L293D (motor driver chip), turn one side ON, which turns the motor into one direction (pin A) and vice versa (pin B).
# To turn the motor ON, there is a (pin Enable), labelled (pin E). 
###
ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
)

def setup_pwm():
    print(Fore.GREEN + "[INFO]: pwm Start." + Fore.WHITE)


# driving forwards

array_left_pwm = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
array_right_pwm = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]

def pwm_start():
        
    newValue_left_pwm = getSonar_left()
    newValue_right_pwm = getSonar_right()

    array_left_pwm.pop()
    array_left_pwm.insert(0, newValue_left_pwm)

    distance_left_pwm = statistics.mean(array_left_pwm)

    array_right_pwm.pop()
    array_right_pwm.insert(0, newValue_right_pwm)

    distance_right_pwm = statistics.mean(array_right_pwm)

        


    if int(distance_left_pwm) <= 20 and int(distance_right_pwm) <= 20:
        print(Fore.RED + "Stopping motor, both sensors activated." + Fore.WHITE + str(distance_left_pwm) + ".." + str(distance_right_pwm))
        ser.write(
            bytes("s", "utf-8"))
        sys.exit()
    else:
        ser.write(bytes("f", "utf-8"))
            

# loop all
def loop_all():
    while(True):
        loop_left()
        loop_right()
        pwm_start()
# --------------------------------------------------
# # socket server setup

# def infinite():
#     while True:
#         yield

# # create a socket server that sends the result of the sensors and motors to the client
# def setup_socket():
#     print(Fore.GREEN + "[INFO]: Socket server start." + Fore.WHITE)
#     HOST = ''  # Symbolic name meaning all available interfaces
#     PORT = 4444  # Arbitrary non-privileged port
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     print('Connected by', addr)

    



#     for __ in infinite():

#         leftUR_send = str(getSonar_left())
#         rightUR_send = str(getSonar_right())
#     # servo_send = str(servoWrite())

#         ur_left_bytes = bytes(leftUR_send, "utf-8")
#         ur_right_bytes = bytes(rightUR_send, "utf-8")
#     #   servo_bytes = bytes(servo_send, "utf-8")

#         data_UR_left  =  b"s UR left     ::  " + ur_left_bytes
#         data_UR_right =  b"s UR right    ::  " + ur_right_bytes
#     #    data_servo    =  b"s servo angle ::  " + servo_bytes


#         print(Fore.WHITE + "[INFO]: Socket server attempting to send data." + Fore.WHITE)
#         print(Fore.GREEN + "[INFO]: Socket server data sent." + Fore.WHITE)
#         # print(data)
#         time.sleep(0.5)
#         conn.send(data_UR_left  + b"\n")
#         time.sleep(0.5)
#         conn.send(data_UR_right + b"\n")
#         time.sleep(0.5)
#    #     conn.send(data_servo    + b"\n")
#     conn.close()
#     s.close()

# --------------------------------------------------

# --------------------------------------------------
# main                                         ........................
if __name__ == '__main__':
    
    print(Fore.GREEN + "[INFO] pwm setup OK." + Fore.WHITE)
    print("[INFO] Trying to setup UR sensors...")
    setup_left()
    time.sleep(1)
    
    print(Fore.GREEN + "[INFO] Left UR sensor setup OK." + Fore.WHITE)
    setup_right()
    time.sleep(1)
    
    print(Fore.GREEN + "[INFO] Right UR sensor setup OK." + Fore.WHITE)
    time.sleep(1)

    print(Fore.CYAN + "[INFO] Initializing..." + Fore.WHITE)
    print("[INFO] Trying to setup pwm...")
    setup_pwm()
    time.sleep(1)
    
    print("[INFO] Trying to setup servo...")
    setup_servo()
    time.sleep(1)
    
    print(Fore.GREEN + "[INFO] Servo setup OK." + Fore.WHITE)
    time.sleep(1)

    print("[INFO] Trying to setup socket...")
  #  setup_socket()
    time.sleep(1)

    print(Fore.GREEN + "[INFO] Socket OK." + Fore.WHITE)
    time.sleep(2)
    
    print(Fore.MAGENTA + "[START] Setup complete, moving on to main loop." + Fore.WHITE)
    time.sleep(2)

    # fishlog initialization
    print(Fore.MAGENTA + "[INFO] Initializing fishlog..." + Fore.WHITE)
    sys.stdout = fishlog("fishlog_car.log")
    sys.stderr = fishlog_logerr("fishlog_car_err.log")
    print(Fore.GREEN + "[INFO] Fishlog initialized." + Fore.WHITE)
    print("[INFO] Starting main loop.")
    try:
        loop_all()
    


    except KeyboardInterrupt:
        print("[INFO] Keyboard interrupt detected, exiting.")
        p.stop()
        GPIO.cleanup()
        print("[INFO] GPIO cleanup complete.")
        print(Fore.YELLOW + "[INFO] Program exiting." + Fore.WHITE)
        sys.exit()
    except Exception as e:
        print(Fore.RED + "[ERROR] Exception detected, exiting." + Fore.WHITE)
        print("" + str(e))
        p.stop()
        GPIO.cleanup()
        print("[INFO] GPIO cleanup complete.")
        print(Fore.YELLOW + "[INFO] Program exiting." + Fore.WHITE)
        sys.exit()
