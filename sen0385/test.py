#!/bin/env python3

import time
import board
from busio import I2C
import adafruit_sht31d

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
sht31d = adafruit_sht31d.SHT31D(i2c)

while True :
    print("Tempereature : %0.1f C"      % sht31d.temperature)
    print("Humidity     : %0.1f %%"     % sht31d.relative_humidity   )
    print("=============================")
    
    time.sleep(1)
