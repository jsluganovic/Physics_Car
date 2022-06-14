# mateo 
print("Mateo ist ein Thunfisch.")
# fishlog init
import sys
import datetime
from time import sleep

class Color(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'
    # add radients
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
                 _
                 )_ `.
                )_ `. :
               )_ `. `|
              )_ `.` /
             )_ `-.` |
            )_ `-.` ` :
             )_.- ` `  :
              )_.-` `   :
               )_.-`\ /\ :
                )_.-| \O  :
                    |  \   :
          _        /   /    \        _
         ) `-._   / /O\  /O\ \   _.-` (
        )      `-/  `-'  `-'  \-`      (
        )     _.-|    __      |-._     (
         )_.-`   \ .-'  `-._  /   `-._(
                  \ `-.__.--`/
                   `-._  _.-"
                       ``
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
        pass
# create a class that logs the terminal output to a file
class fishlog(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

# kira init
print("""
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


""")
#libs
from colorama import Fore
import RPi.GPIO as GPIO
import time 
import logging 
import socket
import sys
#----------------------------------------------------------------
# socket server? 

# servo setup
#----------------------------------------------------------------
OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
servoPin = 12                       # GPIO18
# !Attention! change 18th pin 

def map(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup_servo():
    global p
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
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

def destroy_servo():
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':     #Program start from here
    print (Fore.GREEN + "[INFO] Servo start." + Fore.WHITE)
    setup_servo()
    try:
        loop_servo()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy_servo()

# ----------------------------------------------------

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

def loop_left():
    while(True):
        distance_left = getSonar_left()
        # print ("UR L:: The distance is : %.2f cm"%(distance_left))

        if int(distance_left) <= 20:
            
            servoWrite(20) # rotate the servo by 20 degrees 
            time.sleep(1) # wait for one second, then rotate servo back to 0 degrees
            servoWrite(-20) # rotate the servo back to original position 
            #!ATTENTION: check if this works. 
            return print(Fore.BLUE + "Object detected LEFT, turning RIGHT." + Fore.WHITE)
        else:
            print("UR L:: The distance is : %.2f cm"%(distance_left))
        time.sleep(1) # maybe dont need this ():P


if __name__ == '__main__':     #program start from here
    setup_left()
    try:
        loop_left()
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource

# right sensor

trigPin_right = 16
echoPin_right = 18
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

def loop_right():
    while(True):
        distance_right = getSonar_right()
        # print ("UR L:: The distance is : %.2f cm"%(distance_left))

        if int(distance_right) <= 20:
            servoWrite(-20) # rotate the servo by 20 degrees 
            time.sleep(1) # wait for one second, then rotate servo back to 0 degrees
            servoWrite(20) # rotate the servo back to original position 
            #!ATTENTION: check if this works.
            return print(Fore.BLUE + "Object detected RIGHT, turning LEFT." + Fore.WHITE)
             
        else:
            print("UR R:: The distance is : %.2f cm"%(distance_right))
        time.sleep(1) # maybe dont need this ():P


if __name__ == '__main__':     #program start from here
    setup_right()
    try:
        loop_right()
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource


#----------------------------------------------------------------

# PCM Motor setup 

GPIO.setmode(GPIO.BOARD)
###
# General Info: With the usage of L293D (motor driver chip), turn one side ON, wich turn the motor into one direction (pin A) and vice versa (pin B).
# To turn the motor ON, there is a (pin Enable), labelled (pin E). 
###

Motor1A = 16    # pin 16 (GPIO23)
Motor1B = 18    # pin 18 (GPIO24)
Motor1E = 22    # pin 22 (GPIO11)

def setup_pcm():
    print(Fore.GREEN + "[INFO]: PCM Start." + Fore.WHITE)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

# driving forwards

distance_left_motorUr = getSonar_left()
distance_right_motorUr = getSonar_right()

def pcm_start():
    while distance_left_motorUr and distance_right_motorUr <= str(20):
        
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)

    else: 
        print(Fore.RED + "Stopping motor, both sensors activated." + Fore.RED)
        GPIO.output(Motor1E, GPIO.LOW)


# --------------------------------------------------
# socket server setup

# create a socket server that sends the result of the ultrasonic sensor to the client
def setup_socket():
    print(Fore.GREEN + "[INFO]: Socket server start." + Fore.WHITE)
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 4444  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    data_UR_left  =  b"s UR left     ::  " + getSonar_left().to_bytes(4, byteorder='big')
    data_UR_right =  b"s UR right    ::  " + getSonar_right().to_bytes(4, byteorder='big')
    data_servo    =  b"s servo angle ::  " + servoRead().to_bytes(4, byteorder='big')

    while 1:

        print(Fore.WHITE + "[INFO]: Socket server attempting to send data." + Fore.WHITE)
        print(Fore.GREEN + "[INFO]: Socket server data sent." + Fore.WHITE)
        # print(data)
        time.sleep(0.5)
        conn.send(data_UR_left  + b"\n")
        time.sleep(0.5)
        conn.send(data_UR_right + b"\n")
        time.sleep(0.5)
        conn.send(data_servo    + b"\n")
    conn.close()
    s.close()



# --------------------------------------------------
# main 

if __name__ == '__main__':
    print(Fore.CYAN + "[INFO] Initializing..." + Fore.WHITE)
    print("[INFO] Trying to setup PCM...")
    # setup_pcm()
    time.sleep(1)
    print(Fore.GREEN + "[INFO] PCM setup OK." + Fore.WHITE)
    print("[INFO] Trying to setup UR sensors...")
    # setup_left()
    time.sleep(1)
    print(Fore.GREEN + "[INFO] Left UR sensor setup OK." + Fore.WHITE)
    # setup_right()
    time.sleep(1)
    print(Fore.GREEN + "[INFO] Right UR sensor setup OK." + Fore.WHITE)
    time.sleep(1)
    print("[INFO] Trying to setup servo...")
    # setup_servo()
    time.sleep(1)
    print(Fore.GREEN + "[INFO] Servo setup OK." + Fore.WHITE)
    time.sleep(2)
    print(Fore.MAGENTA + "[START] Setup complete, moving on to main loop." + Fore.WHITE)
    time.sleep(2)

    # fishlog initialization
    print(Fore.MAGENTA + "[INFO] Initializing fishlog..." + Fore.WHITE)
    sys.stdout = fishlog("fishlog_car.log")
    print(Fore.GREEN + "[INFO] Fishlog initialized." + Fore.WHITE)
    print("[INFO] Starting main loop.")
    try:
        while True:
            setup_socket()
            pcm_start()
            time.sleep(1)
            getSonar_left()
            getSonar_right()
            loop_left()
            loop_right()


    except KeyboardInterrupt:
        print("[INFO] Keyboard interrupt detected, exiting.")
        # GPIO.cleanup()
        print("[INFO] GPIO cleanup complete.")
        print(Fore.YELLOW + "[INFO] Program exiting." + Fore.WHITE)
        sys.exit()
    except Exception as e:
        print(Fore.RED + "[ERROR] Exception detected, exiting." + Fore.WHITE)
        print("" + str(e))
       #GPIO.cleanup()
        print("[INFO] GPIO cleanup complete.")
        print(Fore.YELLOW + "[INFO] Program exiting." + Fore.WHITE)
        sys.exit()
