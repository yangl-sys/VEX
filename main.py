#region VEXcode Generated Robot Configuration
from vex import *
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

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

def autonomous():
    pass

def driver_control():
    while True:
        LR = (controller_1.axis4.position() ** 3)/10000
        UD = (controller_1.axis3.position() ** 3)/10000
        Leftdtrain.spin(FORWARD,UD+LR,VOLT)
        Rightdtrain.spin(FORWARD,UD-LR,VOLT)

competition = Competition(driver_control,autonomous)