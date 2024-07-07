from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = Servo(8, pin_factory=factory)

servo.mid()
servo.min()
servo.max()