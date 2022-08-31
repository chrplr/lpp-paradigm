import sys
import time

import expyriment as xp

trig_port = xp.io.ParallelPort(address='0x0378')
trig_port.send(0)

def send_start():
	trig_port.send(1)

def send_stop():
	trig_port.send(0)

#import serial
# os = sys.platform
# if os.startswith('linux'):
#     outport = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)
# elif os.startswith('win'):
#     outport = serial.Serial(0, baudrate=9600, timeout=3.0)
# elif os.startswith('darwin'):  # Mac OS X
#     outport = serial.Serial(0, baudrate=9600, timeout=3.0)
# else:
#     print("Unknown os " + os)

# outport.write('(000;000)')


# def send_start_code():
#     outport.write('(000;007)')


# def send_stop_code():
#     outport.write('000;031')


# def meg_trigger_close():
#     outport.close()


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

    
    
    
