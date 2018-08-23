import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) # domain name, port number

conn.ehlo() # starts connection

conn.starttls() # starts encryption

conn.login('testemailforatbswp@gmail.com', 'swordfish') # logs in 

conn.sendmail(
    'testemailforatbswp@gmail.com', # from email address
    'testemailforatbswp@gmail.com', # to email address

conn.quit() # quits