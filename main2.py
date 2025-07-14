#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Constants
wheel_diameter = 55.5
axle_track = 104
BLACK = 1
WHITE = 99
threshold = (BLACK + WHITE) / 2
LINE_FOLLOW_SPEED = 80
MAZE_SPEED = 120
PROPORTIONAL_GAIN = 1.3

ev3 = EV3Brick()

left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
pickup_motor = Motor(Port.C)
gyro = GyroSensor(Port.S3)
line_sensor = LightSensor(Port.S4)
color_sensor = ColorSensor(Port.S2)
ultrasonic = UltrasonicSensor(Port.S1)

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# --- PID Turn Function ---
def pid_turn_to_angle(target_angle, kp=1.2, ki=0, kd=0.5, tolerance=2, max_speed=100):
    integral = 0
    last_error = 0

    while True:
        current_angle = gyro.angle()
        error = target_angle - current_angle
        integral += error
        derivative = error - last_error
        last_error = error

        turn_speed = kp * error + ki * integral + kd * derivative
        turn_speed = max(-max_speed, min(max_speed, turn_speed))

        robot.drive(0, turn_speed)

        if abs(error) < tolerance:
            break

        wait(20)

    robot.stop()

# --- Ultrasonic Driving Command ---
def drive_until(target_distance_cm, speed=MAZE_SPEED):
    """
    Drive forward until the ultrasonic sensor reads less than or equal to target_distance_cm.
    """
    while True:
        distance = ultrasonic.distance() / 10  # convert mm to cm
        if distance <= target_distance_cm:
            robot.stop()
            break
        robot.drive(speed, 0)
        wait(20)
    robot.stop()

def driveb_until(target_distance_cm, speed=MAZE_SPEED):
    """
    Drive backward until the ultrasonic sensor reads less than or equal to target_distance_cm.
    """
    while True:
        distance = ultrasonic.distance() / 10  # convert mm to cm
        if distance <= target_distance_cm:
            robot.stop()
            break
        robot.drive(-speed, 0)  # negative speed to go backwards
        wait(20)
    robot.stop()


# --- Line Following ---
gyro.reset_angle(0)
wait(500)

while True:
    if color_sensor.color() == Color.RED:
        ev3.speaker.beep()
        break

    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation * 2.5
    robot.drive(LINE_FOLLOW_SPEED, turn_rate)
    wait(10)

# --- Post-line following: Increase speed ---
pid_turn_to_angle(0)
wait(500)
robot.settings(straight_speed=MAZE_SPEED)

# --- Maze Driving Sequence using PID and Ultrasonic ---
drive_until(15.6) 
pid_turn_to_angle(-90) 

drive_until(41.2)
pid_turn_to_angle(0)

drive_until(32.0)
pid_turn_to_angle(90)

drive_until(23.6)
ev3.speaker.say("Ball detected")

# Faster pickup motor
pickup_motor.run_angle(200, 150, wait=True)  # speed=200

ev3.speaker.beep()

driveb_until(39.7)
pid_turn_to_angle(0)

driveb_until(55.1)


pid_turn_to_angle(-90)
drive_until(22.5)

pid_turn_to_angle(90)
drive_until(22.5)

driveb_until(44.3)
pid_turn_to_angle(0)

driveb_until(65)
robot.stop()




# Example of driving until within 10cm of obstacle
# drive_until(10)