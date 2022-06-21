import RPi.GPIO as GPIO
import time
from colorama import Fore
import sys

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
            
            # servoWrite(20) # rotate the servo by 20 degrees 
            time.sleep(1) # wait for one second, then rotate servo back to 0 degrees
            #servoWrite(-20) # rotate the servo back to original position 
            #!ATTENTION: check if this works. 
            print(Fore.BLUE + "Object detected LEFT, turning RIGHT." + Fore.WHITE)
        else:
            print("UR L:: The distance is : %.2f cm"%(distance_left))
        time.sleep(1) # maybe dont need this ():P

if __name__ == "__main__":
    setup_left()
    try:
        getSonar_left()
        loop_left()
    except KeyboardInterrupt:
        print("[INFO] Keyboard interrupt detected, exiting.")
        
        sys.exit()
    except Exception as e:
        print(e)
        print("[INFO] GPIO cleanup complete.")
        sys.exit() 