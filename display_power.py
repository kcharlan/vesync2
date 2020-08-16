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

# Get energy usage data
manager.update_energy()

# Display outlet device information
for device in manager.outlets:
    print( "" )
    device.display()
