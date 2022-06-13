import time
import sys
from colorama import Fore
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
    