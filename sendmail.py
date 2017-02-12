import smtplib
from_addr = 'trudyanncampbell.402@gmail.com'
to_addr = 'necroaj@gmail.com'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{} 
"""
from_name = 'Ongel'
to_name = 'trudy'
subject = 'I love web'
msg ='Web programming is the best :-)'

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed)
username = 'jayboi1da@gmail.com'
password = 'vbbftpswrygbtgvo'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()