import RPi.GPIO as GPIO
import time

pinoLed = 12
cont = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

print("------------ Inicio ------------")
for i in range(cont):
    GPIO.output(pinoLed, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pinoLed, GPIO.LOW)
    time.sleep(1)
    i = i+1
    print("Piscou... " + str(i) + " de " + str(cont) + "")
print("-------------- Fim -------------")
GPIO.cleanup()
