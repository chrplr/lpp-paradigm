# Handling three cases:
# Linux OS
# Windows
# MAC OS X

import os
import sys
import serial
import time

os_ = sys.platform

if os_.startswith('linux'):

    from expyriment import io
    p1 = io.ParallelPort('/dev/paraport1')

    def send_start_code(p1): p1.send(1)

    def send_stop_code(p1): p1.send(0)

    def meg_trigger_close(): p1.close()

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
    for i in range(4):
        print('start')
        send_start_code()
        time.sleep(1)
        print('stop')
        send_stop_code()
        time.sleep(1)
    meg_trigger_close()
