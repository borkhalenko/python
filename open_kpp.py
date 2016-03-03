#date: 03.03.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires pyserial python library
#https://pythonhosted.org/pyserial/index.html
#install: pip install pyserial
import ctypes
import sys

PORT_SPEED = 4800
OPEN_MESSAGE = b"GRNgrn"
CLOSE_MESSAGE = b"REDred"

def __main__():
    port = 0
    try:
        import serial
    except Exception as e:
        mess = "Cannot import serial lib (did you do in cmd 'pip install pyserial?').\n"+"Error message: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)

    if (len(sys.argv)<2):
        mess = "Bad parameters. Use '"+__file__+" COMXXX 1' to open, '"+__file__+" COMXXX 0' to close."
        ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)
        exit()

    try:
        port = serial.Serial(sys.argv[1], PORT_SPEED, serial.EIGHTBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE)
    except Exception as e:
        mess = "Error when try to open port:"+sys.argv[1]+"\n"+"Error message: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)
        exit()
    try:
        if (sys.argv[2]=="1"):
            port.write(OPEN_MESSAGE)
        else:
            if (sys.argv[2]=="0"):
                port.write(CLOSE_MESSAGE)
            else:
                mess = "Bad parameter 2 (use only 1 to open, 0 to close).\n"
                ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)
                port.close()
                exit()
    except Exception as e:
        mess = "Error when writing the message to the port.\n"+"Error message: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)
        port.close()
        exit() 
    port.close()

__main__()
        
            
        

