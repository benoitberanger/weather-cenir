#!/bin/env python3

import time
import board
from busio import I2C
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ain0 = AnalogIn(ads, ADS.P0)

# sensor values : HIH-4000-001
Vs = 3.3 # Volt
slope = 0.0062
offcet = 0.16

while True :
    value = ain0.value
    voltage = ain0.voltage
    RH = (voltage / Vs - offcet) / slope
    print("ADC : %0.3f V"     % voltage)
    print("RH  : %0.1f %%"     % RH)
    print("=============================")
    
    time.sleep(1)
