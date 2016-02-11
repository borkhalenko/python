from send_email import send
from ftplib import FTP
from settings import ftpserver
from settings import ftpuser
from settings import ftppassword
from settings import basedir
from settings import email_addresses
from settings import email_sender
from settings import email_sender_passwd

try:
    ftp=FTP(ftpserver)
    ftp.login(ftpuser, ftppassword)
except:
    print("Could not connect to the ftp server. Check server address, login and password")
try:
    ftp.cwd(basedir)
except:
    print("Could not change directory to "+basedir)
bad_tt=""
list_of_files = ftp.nlst()
for folder in list_of_files:
    if (folder=='.') or (folder=='..'):
        continue;
    try:
        ftp.cwd(folder+"/E")
        if (len(ftp.nlst())>2):
            bad_tt=bad_tt+"TT"+folder+" "
        ftp.cwd(basedir)
    except:
        print("Couldn't find folder "+folder+"/I in the current directory")
message =""
if bad_tt=="":
    message = "All clients was updated correctly! Yea!"
else:
    message = "We have some problems with clients: "+bad_tt
#message.encode('ascii', 'ignore').decode('ascii')
    #message=repr(message.encode("ascii"))
for email in email_addresses:
    send(email_sender, email_sender_passwd, email, "Check price update for DTRetail clients.", message)
ftp.close()
