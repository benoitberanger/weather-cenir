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

while True :
    value = ain0.value
    voltage = ain0.voltage * 1000
    temp = (voltage - 500)/10
    print("ADC (mV)     : %0.0f mV"     % voltage)
    print("Tempereature : %0.1f C"      % temp)
    print("=============================")
    
    time.sleep(1)
