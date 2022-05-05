import RPi.GPIO as GPIO
import time
from time import sleep

buzzerPin = 12
trigPin = 35
echoPin = 33
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(trigPin, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echoPin) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(echoPin) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

pi_pwm = GPIO.PWM(buzzerPin, 100)
pi_pwm.start(1)

#while True:
    #for duty in range(100,1000,20):
        #pi_pwm.ChangeFrequency(duty)
        #sleep(0.1)
    #sleep(0.5)

while True:
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    newFreq = 1 / dist * 15000
    pi_pwm.ChangeFrequency(newFreq)
    time.sleep(0.5)
