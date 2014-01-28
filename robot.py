from sr import *
from time import sleep
import math



rbt = Robot()
sleepFactor = 4.0


while True:
    markers = rbt.see()
    if len(markers) > 0:
        print("Dist:" + str(markers[0].dist) + " | Angle: " + str(markers[0].centre.polar.rot_y) + " | Angle 2: " + str(markers[0].orientation.rot_y) + "Combined: " + str(markers[0].centre.polar.rot_y - markers[0].orientation.rot_y))
        print(str(markers[0].dist * math.sin(math.radians((markers[0].centre.polar.rot_y - markers[0].orientation.rot_y)))))        
        print(str(markers[0].dist * math.sin(math.radians(90 - (markers[0].centre.polar.rot_y - markers[0].orientation.rot_y)))))
        print(str(markers[0].dist * math.sin(math.radians((markers[0].centre.polar.rot_y - markers[0].orientation.rot_y)))))        
        print(str(markers[0].dist * math.sin(math.radians(90 - (markers[0].centre.polar.rot_y - markers[0].orientation.rot_y)))))
    sleep(sleepFactor)
