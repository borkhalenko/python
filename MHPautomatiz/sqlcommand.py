#date: 16.02.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires pymssql python library
#http://pymssql.org/en/latest/index.html
#install: pip install pymssql

import os
import sys


def __main__():
    #Declaring variables
    current_dir= os.path.dirname(os.path.realpath(__file__))
    output_file_path = current_dir+"\sqlcommand_out.txt"
    error_file_path = current_dir+"\sqlcommand_err.txt"
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
        #from xml2json import json2xml
    except Exception as e:
        err.write("Error when importing some libs. Error message: "+str(e))
        out.close()
        err.close()
        exit()
