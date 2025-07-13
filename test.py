#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()

def test_motor(port):
    try:
        motor = Motor(port)
        ev3.speaker.say(f"Motor on port {port.name} found")
        print(f"Motor on port {port.name} initialized successfully.")
        motor.run_angle(180, 90)  # rotate 90 degrees at 180 deg/s
        motor.stop()
        return True
    except Exception as e:
        print(f"Motor on port {port.name} failed: {e}")
        return False

def test_light_sensor(port):
    try:
        sensor = LightSensor(port)
        value = sensor.reflection()
        ev3.speaker.say(f"Light sensor on port {port.name} found")
        print(f"Light sensor on port {port.name} reflection: {value}")
        return True
    except Exception as e:
        print(f"Light sensor on port {port.name} failed: {e}")
        return False

def test_color_sensor(port):
    try:
        sensor = ColorSensor(port)
        color = sensor.color()
        ev3.speaker.say(f"Color sensor on port {port.name} found")
        print(f"Color sensor on port {port.name} color code: {color}")
        return True
    except Exception as e:
        print(f"Color sensor on port {port.name} failed: {e}")
        return False

def test_gyro_sensor(port):
    try:
        sensor = GyroSensor(port)
        angle = sensor.angle()
        ev3.speaker.say(f"Gyro sensor on port {port.name} found")
        print(f"Gyro sensor on port {port.name} angle: {angle}")
        return True
    except Exception as e:
        print(f"Gyro sensor on port {port.name} failed: {e}")
        return False

def main():
    print("Starting hardware test...\n")

    # Test motors
    test_motor(Port.A)
    test_motor(Port.B)
    test_motor(Port.C)
    test_motor(Port.D)

    # Test sensors
    test_light_sensor(Port.S1)
    test_light_sensor(Port.S4)  # your light sensor is on S4 in your code
    
    test_color_sensor(Port.S2)  # your color sensor
    
    test_gyro_sensor(Port.S3)   # your gyro sensor

    print("\nHardware test complete.")
    ev3.speaker.say("Hardware test complete")

if __name__ == "__main__":
    main()