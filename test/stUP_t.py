import time
import sys
from colorama import Fore
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
    # gradient between pink and blue
    PINK_BLUE = '\033[38;5;13m'



if __name__ == '__main__':
    print(Color.GREEN_RAINBOW + """
        
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
        


    print(Color.CYAN_BOLD + """
                    /`·.¸
                    /¸...¸`:·
                ¸.·´  ¸   `·.¸.·´)
                : © ):´;      ¸  {
                `·.¸ `·  ¸.·´\`·¸)
                    `\\´´\¸.·´

""" + Color.END)
    sleep(1)
    print( """
[INFO] Fishlog initialized.\n""" )
    sleep(1)
    print(  """
[INFO] Starting main event...\n""" )
    sleep(1)
    print( """
[INFO]  Main event started.\n\n\n""" )










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

    print("[INFO] Starting main loop.")
    try:
       # pcm_start()
       # getSonar_left()
       # getSonar_right()
       # loop_left()
       print("start init")

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
    