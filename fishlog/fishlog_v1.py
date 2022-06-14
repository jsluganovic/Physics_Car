import sys
import datetime
from colorama import Fore
import time


class Logger(object):
    def __init__(self, filename="fishlog.log"):
        
        self.terminal = sys.stdout
        self.log = open(filename, "a")
        self.err = sys.stderr
        self.errLog = open(filename + "err.log", "a")
        # print ok into the file once it opens
        self.write("[INFO] Logger initialized.\n")
        self.write("""
   ___              __       ___                       
 /'___\ __         /\ \     /\_ \                      
/\ \__//\_\    ____\ \ \___ \//\ \     ___      __     
\ \ ,__\/\ \  /',__\\ \  _ `\ \ \ \   / __`\  /'_ `\   
 \ \ \_/\ \ \/\__, `\\ \ \ \ \ \_\ \_/\ \L\ \/\ \L\ \  
  \ \_\  \ \_\/\____/ \ \_\ \_\/\____\ \____/\ \____ \ 
   \/_/   \/_/\/___/   \/_/\/_/\/____/\/___/  \/___L\ :
                                                /\____/
                                                \_/__/ v. 1.0 by @Skipper_



""")
        # write the time the file was opened
        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        time = str(time)
        self.log.write( "\n"+ f"[{time}] : " + "\n")
        
        # write all errors to the file
        # if stderr occures write it to the file
        
        
        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        time = str(time)

        self.err.write( "\n"+ f"[{time}] : " + "\n")

        self.errLog.write( "\n"+ f"[{time}] : " + "\n")


    def write(self, message):
        self.terminal.write(message)
        
        # log the time only once, not after every message
     #   if time != time:
      #      self.log.write( "\n"+ f"[{time}] : " + "\n")
       #     self.time = time
        # self.log.write( "\n"+ f"[{time}] : " + "\n")
        self.log.write(message)
        

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

def test():
    print("ok", Fore.D)
    
if __name__ == "__main__":
    sys.stdout = Logger("fishlog.log")
    test()
    