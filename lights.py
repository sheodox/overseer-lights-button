import RPi.GPIO as GPIO
import time
import urllib.request
from datetime import datetime
import json

DEBUG_LOGGING = False

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

def debug_log(msg):
    if (DEBUG_LOGGING):
        print(msg)

def req():
    try:
        request = urllib.request.Request(f'{config["overseer"]}/lights/toggle-several',
                                         data=json.dumps({"groups": config['groups']}).encode('utf8'),
                                         headers={'content-type': 'application/json',
                                                  'authorization': f'Bearer {config["token"]}'})

        debug_log(urllib.request.urlopen(request).read())
    except Exception as e:
        print("Error toggling light groups!")
        print(e)


sequential = 0
try:
    while True:
        if GPIO.input(pin) == False:
            sequential += 1
            time.sleep(0.01)
        else:
            sequential = 0

        if sequential == 4:
            debug_log(f'button pressed at {datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")}')
            req()
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
