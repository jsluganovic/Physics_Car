import RPi.GPIO as GPIO
import time
from colorama import Fore
import statistics
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

        if int(distance_right) <= 20:
            print(Fore.BLUE + "Object detected RIGHT, turning LEFT." + Fore.WHITE)
           # servoWrite(180) # rotate the servo by 20 degrees
            #servoWrite(90)
            #time.sleep(1) # wait for one second, then rotate servo back to 0 degrees
            #!ATTENTION: check if this works.
            
            
                
        else:
            print("UR R:: The distance is : %.2f cm"%(distance_right))        

if __name__ == "__main__":
    setup_right()
    while True:
        loop_right()
