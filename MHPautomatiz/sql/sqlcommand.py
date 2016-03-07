#date: 16.02.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#this script requires pymssql python library
#http://pymssql.org/en/latest/index.html
#install: pip install pymssql

import os
import sys
import ctypes
import json

SHOW_MESSAGEBOX = True
ERR_TO_FILE = True
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

def UpdateDatabase(cursor, tab, obj, key_name):
    query = "UPDATE "+tab+" SET "
    field_count = 0
    for field in obj:
        query=query+field+"='"+obj[field]+"'"
        if field_count<(len(obj)-1):
            query = query+", "
        field_count=field_count+1
    query = query+" WHERE "+key_name+"='"+obj[key_name]+"'"
    print(query)
    cursor.execute(query)
    

def InsertDatabase(cursor, tab, obj):
    keys = "("
    for key in obj.keys():
        if (len(keys) > 1):
            keys = keys + ", "
        keys = keys + key
    keys = keys + ")"
    values = "("
    for value in obj.values():
        if (len(values) > 1):
            values = values+ ", "
        values = values + "'"+value+"'"
    values = values + ")"
    query = "INSERT INTO "+tab+" "+keys+" VALUES "+values
    print(query)
    cursor.execute(query)      

def __main__():
    #Declaring variables
    global OUTPUT_FILE
    global ERROR_FILE
    global SQL_CONNECTION
    current_dir= os.path.dirname(os.path.realpath(__file__))
    output_file_path = current_dir+"\sqlcommand_out.txt"
    error_file_path = current_dir+"\sqlcommand_err.txt"
    params = 0
    cursor = 0
    key_names = set()
    key_name = ''

    #Open the file to write result into it
    try:
        OUTPUT_FILE = open(output_file_path, 'w', encoding='utf-8')
    except:
        Report("Cannot open the file "+output_file_path+" for write.")
        Finalise()

    #Open the file to write errors into it
    try:
        ERROR_FILE = open(error_file_path, 'w', encoding='utf-8')
        ERROR_FILE.write("Hello")
    except:
        Report("Cannot open the file "+error_file_path+" for write.")
        Finalise()

    #Importing support libraries
    try:
        import pymssql
    except Exception as e:
        Report("Error when importing some libs. Error message: "+str(e)+".")
        Finalise()

    #Trying to parse json data    
    try:
        params = json.loads(str(sys.argv[1]))	
    except Exception as e:
        Report("Error when parsing input json string. Error message: "+str(e)+".")
        Finalise()

    #Trying to connect to the sql database
    try:
        connection = pymssql.connect(params["server"], params["user"], params["password"], params["dbname"])
        cursor = connection.cursor(as_dict=True)
    except Exception as e:
        Report("Could not connect to the database "+params["dbname"]+" Error message: "+str(e)+".")
        Finalise()

    try:
        key_name = params['key_name']
    except Exception as e:
        Report("Error when getting param 'key_name' from json. Error message: "+str(e)+".")
        
    #Try to execute a sql query
    try:
        cursor.execute("SELECT * FROM [dbo].["+params['tabname']+"]")
        for e in cursor:
            key_names.add(e[key_name])
    except Exception as e:
        Report("Error when getting a SELECT query to the database. Error message: "+str(e)+".")
        Finalise()
    try:
        tab="dbo.["+params['tabname']+"]"
        for obj in params['data']:
            if (obj[key_name] in key_names):
                UpdateDatabase(cursor, tab, obj, key_name)
            else:
                InsertDatabase(cursor, tab, obj)
        connection.commit()
    except Exception as e:
        Report("Error when updating the database (INSERT INTO/UPDATE SET). Error message: "+str(e)+".")
        Finalise()

    Finalise()

__main__()    
    
    
    
        
    
