from colorama import Fore
import socket 
import sys
import time

def setup_socket():
    print(Fore.GREEN + "[INFO]: Socket server start." + Fore.WHITE)
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 4444  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    data_UR_left  =  b"s UR left     ::  "
    data_UR_right =  b"s UR right    ::  "
    data_servo    =  b"s servo angle ::  "

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



if __name__ == '__main__':
    setup_socket()
    print(Fore.YELLOW + "[INFO]: Program exiting." + Fore.WHITE)
    sys.exit()
