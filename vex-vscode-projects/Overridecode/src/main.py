#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()
green = GearSetting.RATIO_18_1
red = GearSetting.RATIO_36_1
# Robot configuration code
controller_1 = Controller(PRIMARY)
Leftdtrain_motor_a = Motor(Ports.PORT1, green, False)
Leftdtrain_motor_b = Motor(Ports.PORT9, green, False)
Leftdtrain = MotorGroup(Leftdtrain_motor_a, Leftdtrain_motor_b)
Rightdtrain_motor_a = Motor(Ports.PORT11, green, False)
Rightdtrain_motor_b = Motor(Ports.PORT19, green, False)
Rightdtrain = MotorGroup(Rightdtrain_motor_a, Rightdtrain_motor_b)
claw_motor = Motor(Ports.PORT3, green, False)
arm_motor_a = Motor(Ports.PORT7,red,False)
arm_motor_b = Motor(Ports.PORT17,red,False)
arm = MotorGroup(arm_motor_a, arm_motor_b)

claw_motor.set_stopping(HOLD)
Leftdtrain.set_stopping(HOLD)
Rightdtrain.set_stopping(HOLD)
arm.set_stopping(HOLD)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

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
    pass

when_started1()

def autonomous():
    wheel_circumference_mm = 320 * 0.75
    def drive(distance_mm, direction):
        degrees = (distance_mm / wheel_circumference_mm) * 360
        Leftdtrain.spin_for(direction, -1*degrees, DEGREES, wait=False)
        Rightdtrain.spin_for(direction, degrees, DEGREES)
    
    def drop():
        claw_motor.spin_for(REVERSE, 20, DEGREES)

    def spinarm(degree,direction):
        arm.spin_for(direction,degree*7) 
    claw_motor.stop(HOLD)
    spinarm(45,FORWARD)
    drive(1700, FORWARD)
    spinarm(35,REVERSE)
    drop()
    spinarm(10,FORWARD)

def driver_control():
    while True:
        close = True
        LR = (controller_1.axis3.position() ** 3)/10000
        UD = (controller_1.axis4.position() ** 3)/10000
        Leftdtrain.spin(FORWARD,UD-LR)
        Rightdtrain.spin(FORWARD,UD+LR)
        def claw_toggle():
            nonlocal close
            if close == True:
                claw_motor.spin_for(FORWARD,20,DEGREES,100,PERCENT,False)
                close = False
            else:
                claw_motor.spin_for(REVERSE,20,DEGREES,100,PERCENT,False)
                close = True
        controller_1.buttonR1.released(claw_toggle)
        arm.spin(FORWARD,controller_1.axis2.position())

competition = Competition(driver_control,autonomous)