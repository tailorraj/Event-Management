import smtplib
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def send_mail(receiver):
  sender = "eventmanage43@gmail.com"
  msg = MIMEMultipart('related')
  msg['Subject'] = "Qr Code"
  msg['From'] = sender
  msg['To'] = receiver

  html = """\
  <html>
    <head></head>
      <body>
        <img src="cid:image1" alt="Logo" style="width:250px;height:250px;"><br>
        <p><h4 style="font-size:15px;">Your Entry Barcode</h4></p>           
      </body>
  </html>
  """
  # Record the MIME types of text/html.
  part2 = MIMEText(html, 'html')

  # Attach parts into message container.
  msg.attach(part2)

  # This example assumes the image is in the current directory
  fp = open('sample_qr.jpg', 'rb')
  msgImage = MIMEImage(fp.read())
  fp.close()

  # Define the image's ID as referenced above
  msgImage.add_header('Content-ID', '<image1>')
  msg.attach(msgImage)

  try:
      smtpObj = smtplib.SMTP('smtp.gmail.com',587)
      smtpObj.starttls()
      smtpObj.login(sender,"event@12345")
      # msg = MIMEMultipart()
      # msg['From'] = sender
      # msg['To'] = receiver
      # msg['Subject'] = "QR Code"
      # msg.attach(MIMEText(body, 'plain'))
      text = msg.as_string()
      smtpObj.sendmail(sender,receiver,text)
      smtpObj.quit()
      print("Successfully sent email")
  except SMTPException:
      print("Error Occured while sending mail")

  # Send the message via local SMTP server.