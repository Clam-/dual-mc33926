from __future__ import print_function
import time
from dual_mc33926 import motors, MAX_SPEED

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1000)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1000)) + [0]

test_reverse_speeds = list(range(0, -MAX_SPEED, -1000)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1000)) + [0]

try:
    motors.enable()
    motors.setSpeeds(0, 0)

    print("\nMotor 1 forward: ")
    for s in test_forward_speeds:
        motors.motor1.setSpeed(s)
        print(s, end="")

    print("\nMotor 1 reverse: ")
    for s in test_reverse_speeds:
        motors.motor1.setSpeed(s)
        print(s, end="")

    print("\nMotor 2 forward: ")
    for s in test_forward_speeds:
        motors.motor2.setSpeed(s)
        print(s, end="")

    print("\nMotor 2 reverse: ")
    for s in test_reverse_speeds:
        motors.motor2.setSpeed(s)
        print(s, end="")

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
  motors.disable()
