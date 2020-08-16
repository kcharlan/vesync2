# Usage of Vesync v2 module

## Description
The purpose of this project was to use the Pypi Vesync v2 module to see if I could control my power outlets, and gather the energy data from them. 

This experiment was successful. Hence saving this for posterity.

The Pypi reference for the library was here: https://pypi.org/project/pyvesync-v2/

There was a v1 interface, but I skipped it since this newer one was present, and it worked. I suspect the v1 is the old Kasa API, and will be deprecated soon (if it isn't already).

## How to run

1) Create a virtual environment. e.g. `virtualenv env`
2) Activate the virtual environment. e.g. `source env/bin/activate`
3) Install the requirements. e.g. `pip install -r requirements.txt`
4) Set up two environment variables with needed login info:

    EMAIL - the email address you login to Vesync with

    PASSWD - the password you use with the email address to sign in to Vesync app

4) Run the appropriate script. e.g. `./display_power.py`


## Files

### display_power.py
This is a pared-down version of example.py. It just connects in and pulls the power stats, and displays them for each outlet.

### example.py
This was a general example built out of the documentation. I found the second outlet in my list was my front room light. 

Used this test to:
- turn on my front room light for a few seconds, then turn it off again
- pull and display the power stats for all my outlets

### power-results.txt
This is a captured output from a run of the display_power.py routine. It gives an example of the type of output you can expect from display_power.py.