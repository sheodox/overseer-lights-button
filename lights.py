import RPi.GPIO as GPIO
import time
import urllib.request
from datetime import datetime
import json

try:
    file = open('config.json')
    config = json.load(file)
    file.close()
except FileNotFoundError:
    print('missing configuration file')

print('Overseer lights button started')
GPIO.setmode(GPIO.BOARD)

pin = 7
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def req(id):
    print(urllib.request.urlopen(f'http://{config["overseer"]}/lights/toggle/{id}').read())

sequential = 0;
try:
    while True:
        if GPIO.input(pin) == False:
            sequential += 1
            time.sleep(0.01)
        else:
            sequential = 0

        if sequential == 4:
            print(f'button pressed at {datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")}')
            req(1)
            req(2)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

