import sys
import Adafruit_DHT
import time
from firebase import firebase
FBConn=firebase.FirebaseApplication("https://sensor-readings-142b2.firebaseio.com/")


sensor = 11
pin = 17

for ij in range(2000):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    hu=str(humidity)
    tem=str(temperature)
    print("Hmudity is "+hu+"      Temperature is "+tem)
    FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Humidity",hu)
    FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Temperature",tem)


