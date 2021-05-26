import smtplib
from email import encoders
from email.mine.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Emails in question
sending_email = "thembekile47@gmail.com"
receiving_email = "mkhombo.itca@gmail.com"
sending_user='Thembekile'

# Connect to your email provider
server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

# Login
server.login(sending_email, "password")

# Create a message, specify regular email parameters
msg = MIMEMultipart()
msg["from"] = sending_user
msg["To"] = receiving_email
msg["Subject"] = "Testing one two"

with open("new Email.txt", "r") as f:
	message = f.read()

msg.attach(MIMEText(message, "plain"))

# I might want to add an image
imagename = "user.png"
attachment = open(filename, "rb")

# Create a payload object
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

# Encode the image data
encoders.encode_base64(p)
p.add_heade("Content-detachment", f"attachment; filename{filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail(sending_email, receiving_email, text)
