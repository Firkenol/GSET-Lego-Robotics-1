#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()

pickup_motor = Motor(Port.B)

while True:
    pickup_motor.run_angle(100,180,wait=True)


if __name__ == "__main__":
    main()