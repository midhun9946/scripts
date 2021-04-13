# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = sys.argv[3]

toaddr = sys.argv[5]

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = sys.argv[6]

# string to store the body of the mail
body = sys.argv[7]

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = sys.argv[9]
attachment = open(sys.argv[8], "rb")


# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

#p.add_header('Content-Disposition', "attachment;)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP(sys.argv[1], sys.argv[2])
#s = smtplib.SMTP('smtp.googlemail.com', 465)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, sys.argv[4])

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

