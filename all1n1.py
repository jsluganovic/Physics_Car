from UR import distance_out as distanceUR
from UR import distanceUR_left
from UR import distanceUR_right
from servo import servoWrite
print("running setup...")

def canDriveForward():
    if distanceUR <= 20:
        return 0


def objectLeft():
    if int(distanceUR_left) <= 20:
        return True

def objectRight():
    if distanceUR_right <= 20:
        turnLeft()

def turnLeft():
    servoWrite(70) # check if this rotates the motor enough to
    # also this needs to sleep like this for to mins

def turnRight():
    servoWrite(70) # check if this rotates the motor enough to
    # also this needs to sleep like this for to mins


def init():
    while True:
        canDriveForward()
        if objectLeft == True:
            turnRight()
        if objectRight == True:
            turnLeft()


if __name__ == '__main__':     # start
    print("Starting...")
    init()