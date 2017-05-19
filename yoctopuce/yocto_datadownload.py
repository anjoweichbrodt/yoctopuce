import sys
import csv

from yocto_api import *
# from yocto_genericsensor import *
from yocto_temperature import *|
from yocto_wakeupmonitor import *

# laststate = -1

def sendHubtoSleep():
  hub = YWakeUpMonitor.FindWakeUpMonitor("YHUBWLN3-4C866.wakeUpMonitor")
  if hub.isOnline() :
      print('Hub will go to sleep is 5 seconds')
      hub.sleep(5)
  else:
      print('hub is offline')


# download of recorded data

def downloadData(sensor):

    data = sensor.get_recordedData(0,0);

    """
    progress = dataset.loadMore()
    while (progress < 100):
        progress = dataset.loadMore()
    """

    print(data)


#this function will be automatically called a new device comes online,
def deviceArrival(m):
    print('Device arrival : ' +  m.get_serialNumber())
    name = m.get_serialNumber() # name = m.get_logicalName()
    if (name == "METEOMK1-4D54B"): #is currently replacing YHUBWLN3-4C866
         sensor = YSensor.FirstSensor() # sensor = YGenericSensor.FindGenericSensor("METEOMK1-4D54B.genericSensor1")
         downloadData(sensor)
         #sendHubtoSleep()

errmsg=YRefParam()

# No exception please
YAPI.DisableExceptions()


# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

"""
# configure the API to use the meteo hub if available
if YAPI.PreregisterHub("127.0.0.1", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)
"""

# Each time a device com online, deviceArrival will be called
YAPI.RegisterDeviceArrivalCallback(deviceArrival)

print('Hit Ctrl-C to Stop ')

#nothing to do except waiting
while True:
    YAPI.UpdateDeviceList(errmsg) # traps plug/unplug events
    YAPI.Sleep(500, errmsg)   # traps others events
