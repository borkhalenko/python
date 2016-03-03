#date: 03.03.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#Цей скрипт потребує сторонню бібліотеку pyserial
#https://pythonhosted.org/pyserial/index.html
#install from cmd: pip install pyserial

#Параметри:
# 1 - ім'я СОМ-порта
# 2 - команда відкриття (0 - закрити, 1 - відкрити)
#Приклад виклику скрипта
#python.py open_kpp.py COM4 1
#python.py open_kpp.py COM4 0

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
        mess = "Помилка при імпорті бібліотек (можливо, ви забули встановити pyserial?').\n"+"Опис помилки: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Помилка!", 1)

    if (len(sys.argv)<2):
        mess = "Невірні параметри виклику. Потрібно: '"+__file__+" COMXXX 1' щоб відкрити, '"+__file__+" COMXXX 0' щоб закрити."
        ctypes.windll.user32.MessageBoxW(None, mess, "Помилка!", 1)
        exit()

    try:
        port = serial.Serial(sys.argv[1], PORT_SPEED, serial.EIGHTBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE)
    except Exception as e:
        mess = "Помилка відкриття СОМ-порта:"+sys.argv[1]+"\n"+"Опис помилки: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Помилка!", 1)
        exit()
    try:
        if (sys.argv[2]=="1"):
            port.write(OPEN_MESSAGE)
        else:
            if (sys.argv[2]=="0"):
                port.write(CLOSE_MESSAGE)
            else:
                mess = "Невірний параметр 2 (використовуйте 1 щоб відкрити, 0 щоб закрити).\n"
                ctypes.windll.user32.MessageBoxW(None, mess, "Помилка!", 1)
                port.close()
                exit()
    except Exception as e:
        mess = "Помилка при спробі записати в порт.\n"+"Опис помилки: "+str(e)
        ctypes.windll.user32.MessageBoxW(None, mess, "Помилка!", 1)
        port.close()
        exit() 
    port.close()

__main__()
        
            
        

