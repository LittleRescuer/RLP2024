from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

class ServoController:
    def __init__(self):
        factory = PiGPIOFactory()
        self.servo = Servo(8, pin_factory=factory)
        self.servo.mid()
    
    def moveToMin(self):
        self.servo.min()

    def moveToMid(self):
        self.servo.mid()

    def moveToMax(self):
        self.servo.max()
    
    def __del__(self):
        self.servo.detach()
    