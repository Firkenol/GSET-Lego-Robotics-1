#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.nxtdevices import LightSensor
from pybricks.ev3devices import ColorSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

# Constants
wheel_diameter = 55.5
axle_track = 104

BLACK = 1
WHITE = 99
threshold = (BLACK + WHITE) / 2
DRIVE_SPEED = 80

ev3 = EV3Brick()

left_motor = Motor(Port.D)
gyro = GyroSensor(Port.S3)
right_motor = Motor(Port.A)
pickup_motor = Motor(Port.B)
line_sensor = LightSensor(Port.S4)
color_sensor = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

PROPORTIONAL_GAIN = 1.3

while True:
    # Check if red is detected
    if color_sensor.color() == Color.RED:
        robot.stop()
        ev3.speaker.beep()  # Optional: make a sound to confirm stop
        break  # Exit the loop to fully stop

    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation * 2.5
    robot.drive(DRIVE_SPEED, turn_rate)

    wait(10)
    gyro.reset_angle(0)
    robot.straight(303)
    robot.turn(90)
    robot.straight(303)
    robot.turn(-90)
    robot.straight(303)
    ev3.speaker.say("Ball detected")
    pick_up.run_angle(speed,200,wait=True)
    ev3.speaker.beep()
    # robot.straight(-303)
    # robot.turn(-90)
    # robot.straight(606)
    # robot.turn(90)
    # robot.straight(100)
    # robot.straight(-100)
    # robot.turn(-90)
    # robot.straight(303)
    # robot.turn(90)
    # robot.straight(100)
    # robot.straight(-100)