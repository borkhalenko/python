#date: 29.01.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires Requests python library
#http://docs.python-requests.org/en/latest/
#install: pip install requests or easy_install requests

#importing base libraries
import os
import sys

def __main__():
    #Declaring variables
    current_dir= os.path.dirname(os.path.realpath(__file__))
    output_file_path = current_dir+"\getJsonString_out.txt"
    error_file_path = current_dir+"\getJsonString_err.txt"
    resp = ""
    out = 0
    err = 0

    #Open the file to write result into it
    try:
        out = open(output_file_path, 'w', encoding='utf-8')
    except:
        print("Cannot open file "+output_file_path+" for write")

    #Open the file to write errors into it
    try:
        err = open(error_file_path, 'w', encoding='utf-8')
    except:
        print("Cannot open file "+error_file_path+" for write")

    #Importing support libraries
    try:
        import requests
        import base64
        import binascii
        import gzip
        import json
        import JsonParser
        import switch
        #from xml2json import json2xml
    except Exception as e:
        err.write("Error when importing some libs. Error message: "+str(e))
        out.close()
        err.close()
        exit()

    #Getting data from url request
    try:
        requests.packages.urllib3.disable_warnings()
        result = requests.get(sys.argv[1], verify=False)
        resp=result
    except Exception as e:
        err.write("Error when getting data from url request. Check the internet connection and URL's. ")
        err.write("Error message: "+str(e))
        out.close()
        err.close()
        exit()

    #Deleting managed symbol '\' from received string
    result_string=result.text.replace("\\", "")

    #Decoding data from base64
    try:
        result_string=base64.b64decode(result_string)
    except Exception as e:
        err.write("Error when decoding incoming data from base64 encoding")
        err.write("Error message: "+str(e)+" ")
        err.write("Responce string: "+str(resp))
        out.close()
        err.close()
        exit()

    #Unzipping data from archive
    try:
        result_string=gzip.decompress(result_string)
    except Exception as e:
        err.write("Error when unzipping data from archive")
        err.write("Error message: "+str(e))
        out.close()
        err.close()
        exit()

    #Converting byte array to utf-8 string
    try:
        result_string=result_string.decode("utf-8", "ignore")
    except Exception as e:
        err.write("Error when converting byte array to utf-8 string")
        err.write("Error message: "+str(e))
        out.close()
        err.close()
        exit()
    #out.write(result_string)
    #result_string = json2xml(result_string)
    #writing every object to the next line
##    json_obj = json.loads(result_string)
##    obj_len = len(json_obj)
##    for i in json_obj:
##        out.write(str(i))
##        out.write('\n')
####    result_dict=0;
    if sys.argv[2]=='1':
        result_dict=JsonParser.ParseUom(result_string)
    if sys.argv[2]=='2':
        result_dict=JsonParser.ParseGoodsCategories(result_string)
    if sys.argv[2]=='3':
        result_dict=JsonParser.ParseGoodsItems(result_string)
##    else
##        print ("Bad command to parse dictionary from json")

    for item in result_dict:
        out.write(str(item))
        out.write('\n')

    #Close the file
    out.close()
    err.close()

__main__()
    
