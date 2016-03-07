#date: 16.02.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires pymssql python library
#http://pymssql.org/en/latest/index.html
#install: pip install pymssql

from sqlsettings import sqladdress
from sqlsettings import sqluser
from sqlsettings import sqlpassword
from sqlsettings import sqldbname

import os
import sys
import ctypes
import json
import 

SHOW_MESSAGEBOX = True
ERR_TO_FILE = False
OUTPUT_FILE = 0
ERROR_FILE = 0
SQL_CONNECTION = 0

def Report(message):
    if (SHOW_MESSAGEBOX):
        ctypes.windll.user32.MessageBoxW(None, message, "Error!", 1)
    if (ERR_TO_FILE):
        try:
            ERROR_FILE.write(message)
        except Exception as e:
            mess = "Cannot write message to the error file.\n"+"Error message: "+str(e)
            ctypes.windll.user32.MessageBoxW(None, mess, "Error!", 1)

def Finalise():
    try:
        OUTPUT_FILE.close()
    except:
        pass
    try:
        ERROR_FILE.close()
    except:
        pass
    try:
        SQL_CONNECTION.close()
    except:
        pass
    exit()

def __main__():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    files_dir = current_dir+"\E\Articles";
    for file in os.scandir(files_dir):
        if file.is_file():
            print(file.name)
__main__()
    
    
    
    

