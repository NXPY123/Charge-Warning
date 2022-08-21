#!/usr/bin/env python

import psutil
from playsound import playsound



while(psutil.sensors_battery().power_plugged):
    if(psutil.sensors_battery().percent>=80):
        playsound('beep-beep-6151.mp3')



