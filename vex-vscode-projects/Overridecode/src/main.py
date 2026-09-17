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
arm_motor = Motor(Ports.PORT4, green, False)
claw_motor.set_stopping(HOLD)
arm_motor.set_stopping(HOLD)
Leftdtrain.set_stopping(HOLD)
Rightdtrain.set_stopping(HOLD)

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
    wheel_circumference_mm = 320
    one_foot_mm = 304.8

    def drive(distance_mm, direction):
        degrees = (distance_mm / wheel_circumference_mm) * 360
        Leftdtrain.spin_for(direction, -1*degrees, DEGREES, wait=False)
        Rightdtrain.spin_for(direction, degrees, DEGREES)

    def drop():
        claw_motor.spin_for(REVERSE, 80, DEGREES)

    # Tunnel: forward, back, forward, back, then forward.
    claw_motor.stop(HOLD)
    drive(1790, FORWARD)
    drop()

def driver_control():
    while True:
        claw = False
        LR = (controller_1.axis3.position() ** 3)/10000
        UD = (controller_1.axis4.position() ** 3)/10000
        Leftdtrain.spin(FORWARD,UD-LR)
        Rightdtrain.spin(FORWARD,UD+LR)

        if controller_1.buttonR1.pressing():
            claw = not claw
            if claw == True:
                claw_motor.spin_for(FORWARD, 80, DEGREES)
            else:
                claw_motor.spin_for(REVERSE, 80, DEGREES)

        if controller_1.buttonL1.pressing():
            arm_motor.spin(FORWARD,100,PERCENT)

        if controller_1.buttonL2.pressing():
            arm_motor.spin(REVERSE,100,PERCENT)

        wait(20, MSEC)

competition = Competition(driver_control,autonomous)