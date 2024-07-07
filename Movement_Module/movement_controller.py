# Necessary Imports
import RPi.GPIO as GPIO
from time import sleep

# All pins in Raspberry Pi Zero
# Power
PWMA = 7 # Power to Right Wheel
PWMB = 18 

# Standby
STBY = 13

# Signal
AIN1 = 12 # Right Wheel to move forward (raspberry pi in front)
AIN2 = 11 # Right Wheel to move backwards (raspberry pi in back)
BIN1 = 15 # Left Wheel to move forward (raspberry pi in front)
BIN2 = 16 # Left Wheel to move backwards (raspberry pi in back)


class MovementController:
    def __init__(self):
        self.pwm_a = PWMA
        self.pwm_b = PWMB
        self.ain1 = AIN1
        self.ain2 = AIN2
        self.stby = STBY
        self.bin1 = BIN1
        self.bin2 = BIN2

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(PWMA, GPIO.OUT)
        GPIO.setup(PWMB, GPIO.OUT)

        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT)

        GPIO.setup(STBY, GPIO.OUT)

        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)

        GPIO.output(self.pwm_a, GPIO.HIGH)
        GPIO.output(self.pwm_b, GPIO.HIGH)
        GPIO.output(self.stby, GPIO.HIGH)
        print("Movement Controller Initialized")

    def moveForward(self):
        print("Moving Forward")
        self.stop()


        # Right Wheel
        GPIO.output(self.ain2, GPIO.HIGH)
        # Left Wheel
        GPIO.output(self.bin2, GPIO.HIGH)
    
    def moveBackward(self):
        print("Moving Backward")
        self.stop()

        # Right Wheel
        GPIO.output(self.ain1, GPIO.HIGH)
        # Left Wheel
        GPIO.output(self.bin1, GPIO.HIGH)

        

    def moveRight(self):
        print("Moving Right")
        self.stop()

        GPIO.output(self.bin2, GPIO.HIGH)

    def moveLeft(self):
        print("Moving Left")
        self.stop()

        GPIO.output(self.ain2, GPIO.HIGH)

    def stop(self):
        print("Stopping")
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.LOW)

        GPIO.output(self.bin1, GPIO.LOW)
        GPIO.output(self.bin2, GPIO.LOW)
        sleep(0.5) # Stop for 0.5 seconds in order to not mess up the balance

    def __del__(self):
        GPIO.cleanup()
    