import RPi.GPIO as GPIO
from colorama import Fore

import sys

GPIO.setmode(GPIO.BOARD)
###
# General Info: With the usage of L293D (motor driver chip), turn one side ON, which turns the motor into one direction (pin A) and vice versa (pin B).
# To turn the motor ON, there is a (pin Enable), labelled (pin E). 
###

# Motor1A = 16    # pin 16 (GPIO23)
# Motor1B = 18    # pin 18 (GPIO24)
# Motor1E = 22    # pin 22 (GPIO11)

Motor1A = 11    # pin 11 (GPIO17)



def setup_pwm():
    print(Fore.GREEN + "[INFO]: pwm Start." + Fore.WHITE)
    GPIO.setup(Motor1A, GPIO.OUT)


def pwm_start():

    GPIO.output(Motor1A, GPIO.HIGH)

if __name__ == "__main__":
    setup_pwm()
    pwm_start()