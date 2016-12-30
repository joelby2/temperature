#!/usr/bin/env python

import re
import time
import datetime
import LCD1602 as LCD

LCD.init(0x27, 1)

p = re.compile('t=(\d{5})')

try:
  while True:
    with open("/sys/bus/w1/devices/28-031674c922ff/w1_slave", "r") as TempFile:
      temp = p.search(TempFile.read()).group(1)

    LCD.write(0,0,str(datetime.datetime.now()))
    LCD.write(0,1,"%2.1f F (%2.1f C)" % (int(temp)*0.0018+32.0,int(temp)/1000.0))
    time.sleep(1)

except KeyboardInterrupt:
  LCD.clear()
  LCD.write(0,0,'Goodbye you')
  LCD.write(0,1,'See you soon')
  time.sleep(5)
  LCD.clear()
