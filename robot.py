from sr import *
import time
R = Robot()

while True:
    markers = R.see()
    print "I can see", len(markers), "markers:"

    for m in markers:
            print " - The code {0}th is {1} and the distance is {2}".format(m, m.info.code, m.dist)
            R.power.beep(200,0.5)
            time.sleep(1)
    time.sleep(2)
