################################################################

"""Sends email using smtplib"""

################################################################

import smtplib
logininfo = ['jerryvbroker@gmail.com', 'CS121AFinal']

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(logininfo[0],logininfo[1])
server.sendmail(logininfo[0], 'bock@stolaf.edu', "Test")
server.close()
print('done')
