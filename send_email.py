import sys
def send(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    #try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    #server = smtplib.SMTP("smtp-mail.outlook.com",995)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print ('successfully sent the mail')
    #except:
    #    print ('failed to send mail')

#send('hacker.dniprotorg@gmail.com', 'YaRoShFiRmA', sys.argv[1], sys.argv[2], sys.argv[3])
