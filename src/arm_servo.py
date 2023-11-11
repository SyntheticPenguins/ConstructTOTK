import RPi.GPIO as gpio

class ArmServo:
    # class that controls the servo movements
    # three funcs: strike, retract, kill
    def __init__(self, pin):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.OUT)

        self.servo = gpio.PWM(pin, 50)
        self.servo.start(3) # start in the retracted position
        
    def strike(self):
        self.servo.ChangeDutyCycle(9)
    
    def retract(self):
        self.servo.ChangeDutyCycle(3)
    
    def kill(self):
        self.servo.stop()
        gpio.cleanup()
        del self