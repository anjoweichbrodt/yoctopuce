import sys

from yocto_api import *

# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

# configure the API to use the mailbox hub if available
if YAPI.PreregisterHub("172.0.0.1", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

# Each time a device comes online, deviceArrival is called
YAPI.RegisterDeviceArrivalCallback(deviceArrival)

while True:
    YAPI.UpdateDeviceList(errmsg) # traps plug/unplug events
    YAPI.Sleep(500, errmsg)   # traps others events
