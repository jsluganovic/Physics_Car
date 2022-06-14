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



class Logger(object):
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

def test():
    print("ok")
    
if __name__ == "__main__":
    sys.stdout = Logger("fishlog_v2.log")
    test()
    