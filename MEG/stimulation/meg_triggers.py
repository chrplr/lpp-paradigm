# Handling three cases:
# Linux OS
# Windows
# MAC OS X

import os
import sys
import serial
import time
from expyriment import io

os_ = sys.platform

PORT = '/dev/parport1'

# Current :
if os_.startswith('linux'):

    def send_start(initialized,p1 = None): 
        if not initialized:
            p1 = io.ParallelPort(PORT)
        p1.send(1)
        return p1

    def send_stop(p1): 
        p1.send(0)

    def meg_trigger_close(p1): p1.clear()

elif os_.startswith('win'):

    from ctypes import windll

    p = windll.inpout32
    p.Inp32(0x378)
    p.Out32(0x378, 255)

    # lib = ctypes.WinDLL('inpoutx64.dll')
    # outp = lib['Out32']
    # inp = lib['Inp32']

    address = 888  # LPT1
    # value = 255 #raise all pins
    # outp(address, value)

    # address = 899 #LPT2
    # inp(address) #read value

    p.Out32(address, 0)
    # trig_port.send(0)

    def send_start():
        p.Out32(address, 1)

    def send_stop():
        p.Out32(address, 0)

    outport = serial.Serial(0, baudrate=9600, timeout=3.0)

elif os.startswith('darwin'):  # Mac OS X

    outport = serial.Serial(0, baudrate=9600, timeout=3.0)

else:

    print("Unknown os " + os)


def meg_trigger_test():
    time.sleep(1)
    initialized = False
    p1 = None
    for i in range(100):
        print(f'start')
        p1 = send_start(initialized,p1)
        initialized = True
        time.sleep(0.01)
        print(f'stop')
        send_stop(p1)
        time.sleep(0.01)
    meg_trigger_close(p1)
