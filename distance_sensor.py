from time import sleep
from gpiozero import DistanceSensor
dist_sensor = DistanceSensor(echo=13, trigger=6, max_distance=4)
print("Press CTRL-C to exit.\n")
while True:
    print("Distance sensor read %.1f cm." % (dist_sensor.distance * 100))
    sleep(1)