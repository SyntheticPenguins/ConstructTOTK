from arm_servo import ArmServo
from time import sleep

# servo
servo = ArmServo(7)

# main
try:
    while True:
        servo.strike()
        sleep(1)
        servo.retract()
        sleep(1)
except KeyboardInterrupt:
    servo.kill()