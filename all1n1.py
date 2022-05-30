from UR import distance_out as distanceUR
from UR import distanceUR_left
from servo import servoWrite
print("running setup...")

def canDriveForward():
    if distanceUR <= 20:
        return 0


def objectLeft():
    if distanceUR_left <= 20:
        turnRight()

def objectRight():
    if distanceUR_right <= 20:
        turnLeft()

def turnLeft():
    servoWrite(70) # check if this rotates the motor enough to
    # also this needs to sleep like this for to mins