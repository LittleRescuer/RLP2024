from time import sleep
import cv2
from picamera2 import Picamera2
import RPi.GPIO as GPIO

picam2 = Picamera2()
picam2.start()

PWMA = 7
PWMB = 18
AIN1 = 12
AIN2 = 11
STBY = 13
BIN1 = 15
BIN2 = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(STBY, GPIO.OUT)

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.LOW)

GPIO.output(BIN1, GPIO.HIGH)
GPIO.output(BIN2, GPIO.LOW)

GPIO.output(PWMA, GPIO.HIGH)

GPIO.output(PWMB, GPIO.HIGH)

GPIO.output(STBY, GPIO.HIGH)

sleep(5)

GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.HIGH)

GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.HIGH)

GPIO.output(PWMA, GPIO.HIGH)

GPIO.output(PWMB, GPIO.HIGH)

GPIO.output(STBY, GPIO.HIGH)

sleep(5)

GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(PWMA, GPIO.LOW)
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.LOW)
GPIO.output(PWMB, GPIO.LOW)
GPIO.output(STBY, GPIO.LOW)

sleep(5)

i = 0
while i < 10:
    print("Hello World")
    i += 1
    frame = picam2.capture_array()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    cv2.imwrite(f"Image_Test_{i}.jpg", frame)
picam2.close()