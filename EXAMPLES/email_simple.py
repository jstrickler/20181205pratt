#!/usr/bin/env python
import smtplib  # <1>

DEBUG = True  # set to false for production

smtp_user = 'pythonclass'
smtp_pwd = 'pythonr0xx'

sender = 'jstrick@mindspring.com'
recipients = ['jstrickler@gmail.com']
msg = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''

smtpserver = smtplib.SMTP("smtpcorp.com", 2525)  # <2>
smtpserver.login(smtp_user, smtp_pwd)  # <3>
smtpserver.set_debuglevel(DEBUG)  # <4>

try:
    smtpserver.sendmail(
        sender,
        recipients,
        msg
    )  # <5>
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
finally:
    smtpserver.quit()  # <6>
