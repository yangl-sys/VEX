#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
Leftdtrain_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Leftdtrain_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
Leftdtrain = MotorGroup(Leftdtrain_motor_a, Leftdtrain_motor_b)
Rightdtrain_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
Rightdtrain_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
Rightdtrain = MotorGroup(Rightdtrain_motor_a, Rightdtrain_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

def when_started1():
    global myVariable
    pass

when_started1()

def autonomous():
    pass

def driver_control():
    while True:
        LR = (controller_1.axis4.position() ** 3)/10000
        UD = (controller_1.axis3.position() ** 3)/10000
        Leftdtrain.spin(FORWARD,UD+LR,VOLT)
        Rightdtrain.spin(FORWARD,UD-LR,VOLT)

competition = Competition(driver_control,autonomous)