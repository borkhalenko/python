#date: 29.01.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires Requests python library
#http://docs.python-requests.org/en/latest/
#install: pip install requests or easy_install requests

#importing base libraries
import os
import sys
import ctypes

SHOW_MESSAGEBOX = True
ERR_TO_FILE = True
OUTPUT_FILE = 0
ERROR_FILE = 0

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
    exit()
        
def __main__():
    #Declaring variables
    global OUTPUT_FILE
    global ERROR_FILE 
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_file_path = current_dir+"\getJsonString_OUTPUT_FILE.txt"
    error_file_path = current_dir+"\getJsonString_ERROR_FILE.txt"
    resp = ""

    #Open the file to write result into it
    try:
        OUTPUT_FILE = open(output_file_path, 'w', encoding='utf-8')
    except:
        Report("Cannot open file "+output_file_path+" for write")
        Finalise()

    #Open the file to write ERROR_FILEors into it
    try:
        ERROR_FILE = open(error_file_path, 'w', encoding='utf-8')
    except:
        Report("Cannot open file "+error_file_path+" for write")
        Finalise()

    #Importing support libraries
    try:
        import requests
        import base64
        import binascii
        import gzip
        import json
        import JsonParser
        #from xml2json import json2xml
    except Exception as e:
        Report("Error when importing some libs. Error message: "+str(e))
        Finalise()
        

    #Getting data from url request
    try:
        requests.packages.urllib3.disable_warnings()
        result = requests.get(sys.argv[1], verify=False)
        resp=result
    except Exception as e:
        Report("Error when getting data from url request. Check the internet connection and URL's.\n"+"Error message: "+str(e))
        Finalise()

    #Deleting managed symbol '\' from received string
    result_string=result.text.replace("\\", "")

    #Decoding data from base64
    try:
        result_string=base64.b64decode(result_string)
    except Exception as e:
        Report("Error when decoding incoming data from base64 encoding.\n"+" Error message: "+str(e))
        Finalise()

    #Unzipping data from archive
    try:
        result_string=gzip.decompress(result_string)
    except Exception as e:
        Report("Error when unzipping data from archive.\n"+" Error message: "+str(e))
        Finalise()
    
    #Converting byte array to utf-8 string
    try:
        result_string=result_string.decode("utf-8", "ignore")
    except Exception as e:
        Report("Error when converting byte array to utf-8 string.\n"+" Error message: "+str(e))
        Finalise()

    #Parsing a json string to the array of items
    try:
        if sys.argv[2]=='1':
            result_dict=JsonParser.ParseUom(result_string)
        if sys.argv[2]=='2':
            result_dict=JsonParser.ParseGoodsCategories(result_string)
        if sys.argv[2]=='3':
            result_dict=JsonParser.ParseGoodsItems(result_string)
    except Exception as e:
        Report("Error when parsing json data to a text file.\n"+" Error message: "+str(e))
        Finalise()

    for item in result_dict:
        OUTPUT_FILE.write(str(item))
        OUTPUT_FILE.write('\n')

    #Close the file
    OUTPUT_FILE.close()
    ERROR_FILE.close()

__main__()
    
