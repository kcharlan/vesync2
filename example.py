#!/usr/bin/env python3

import os, time
from pyvesync_v2 import VeSync

EMAIL=os.environ.get("EMAIL")
PASSWD=os.environ.get("PASSWD")


if EMAIL is None or PASSWD is None:
    if EMAIL is None:
        print( "Email address must be set in environment variable EMAIL.")
    if PASSWD is None:
        print( "Password must be set in environment variable PASSWD.")
    exit(1)

manager = VeSync(EMAIL, PASSWD)

# NOTE: could not find API doc, and exception not raised
# on a bad login test. So just allowing login errors to
# flow through. Will fail in later code.
manager.login()

# Get/Update Devices from server - populate device lists
manager.update()

# This section was a test - which worked
# was specific to my front room ligt
#
#my_switch = manager.outlets[1] # - front room light
# Turn on the second switch
#my_switch.turn_on()
#time.sleep(3)
# Turn off the second switch
#my_switch.turn_off()


# Get energy usage data
manager.update_energy()

# Display outlet device information
for device in manager.outlets:
    print( "" )
    device.display()
