import socket
from colorama import Fore

print(Fore.CYAN + "[INFO] Initializing..." + Fore.WHITE)

# create a socket client that gets data from the server and prints it to the screen
def client():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 4444
    # connection to hostname on the port.
    s.connect((host, port))
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    # loop to receive data from the socket
    print(Fore.GREEN + "[INFO] Connected to server." + Fore.WHITE)

    while msg:
        ur_word_left = b"s UR left     ::  "
        ur_word_right = b"s UR right    ::  "
        servo_word = b"s servo angle ::  "

        # print the received data
        if ur_word_left in msg:
            print(Fore.LIGHTYELLOW_EX + msg.decode("utf-8") + Fore.WHITE)
        elif ur_word_right in msg:
            print(Fore.LIGHTGREEN_EX + msg.decode("utf-8") + Fore.WHITE)
        elif servo_word in msg:
            print(Fore.LIGHTBLUE_EX + msg.decode("utf-8") + Fore.WHITE)
        
        
        # print(msg.decode('utf-8'))
        # receive the next data packet
        msg = s.recv(1024)
    # close the connection
    s.close()
    
    # Close the socket when done
    print(Fore.YELLOW + "[INFO] Socket closed." + Fore.WHITE)


if __name__ == '__main__':
    client()
