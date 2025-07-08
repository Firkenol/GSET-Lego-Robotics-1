#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
ev3 = EV3Brick()
ev3.screen.print("Hello World")
wait(1000)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
my_robot = DriveBase(left_motor, right_motor, 56, 128)
#my_robot.distance_control.pid(100, 1, 10)
my_robot.straight(100)