#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
Leftdtrain_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_36_1, False)
Leftdtrain_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_36_1, False)
Leftdtrain = MotorGroup(Leftdtrain_motor_a, Leftdtrain_motor_b)
Rightdtrain_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_36_1, False)
Rightdtrain_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_36_1, False)
Rightdtrain = MotorGroup(Rightdtrain_motor_a, Rightdtrain_motor_b)
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)


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
        Leftdtrain.spin_for(direction, degrees, DEGREES, wait=False)
        Rightdtrain.spin_for(direction, degrees, DEGREES)

    def turn_left():
        turn_degrees = 360
        Leftdtrain.spin_for(REVERSE, turn_degrees, DEGREES, wait=False)
        Rightdtrain.spin_for(FORWARD, turn_degrees, DEGREES)

    # Tunnel: forward, back, forward, back, then forward.
    drive(one_foot_mm, FORWARD)
    drive(one_foot_mm, REVERSE)
    drive(one_foot_mm, FORWARD)
    drive(one_foot_mm, REVERSE)
    drive(one_foot_mm, FORWARD)

    # Turn left, travel 12 feet, then move 1 foot in and back out.
    turn_left()
    drive(12 * one_foot_mm, FORWARD)
    drive(one_foot_mm, FORWARD)
    drive(one_foot_mm, REVERSE)

def driver_control():
    while True:
        LR = (controller_1.axis3.position() ** 3)/10000
        UD = (controller_1.axis4.position() ** 3)/10000
        Leftdtrain.spin(FORWARD,UD+LR)
        Rightdtrain.spin(FORWARD,UD-LR)

        if controller_1.buttonR1.pressing():
            claw_motor.spin(FORWARD, 100, PERCENT)
        elif controller_1.buttonR2.pressing():
            claw_motor.spin(REVERSE, 100, PERCENT)
        else:
            claw_motor.stop(HOLD)

        wait(20, MSEC)

competition = Competition(driver_control,autonomous)