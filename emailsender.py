import smtplib
import imghdr
import numpy as np
import pandas as pd
from datetime import datetime
from email.message import EmailMessage

# Load data
df = pd.read_csv("Data.csv", sep=";")

# Access to gmail sender account
password = "yourgmailpassword"
sender_email = "yourgmailaccount@gmail.com"

# Function to send emails


def sendemails(receiver_email, receiver_name, receiver_inst):
    # Plain text and html text of my email
    text = """\
    Dear  {name} ",
    This is simply dummy text of the printing and typesetting industry for sending emails to {institution}. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 
    but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
    sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
    """

    html = """\
    <!DOCTYPE html>
    <html>
      <body>
        <p>Dear {name},</p>
        <p>This is simply dummy text of the printing and typesetting industry for sending emails to {institution}. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
           when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 
           but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
           sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
        </p>
      </body>
    </html>
    """

    # Load attachment file
    file = "attachment.pdf"

    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    # Configure the Message
    message = EmailMessage()
    message["Subject"] = "Subject of the email"
    message["From"] = "Your name"
    message["To"] = receiver_email

    # Set the content of the message incluiding the attachment file and the values of name and institution
    message.set_content(text.format(
        name=receiver_name, institution=receiver_inst))
    message.add_alternative(html.format(
        name=receiver_name, institution=receiver_inst), subtype='html')

    message.add_attachment(file_data, maintype='application',
                           subtype='octet-stream', filename=file_name)

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)


# Looping to send the email and retrieve the info about the time the email was sent
time_list = []
for i in range(df.shape[0]):
    try:
        email = df['Email'][i]
        name = df['Name'][i]
        institution = df['Institution'][i]
        sendemails(receiver_email=email,
                   receiver_name=name,
                   receiver_inst=institution)
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print('Email sent to', email, 'at', time)
        time_list.append(time)
    except:
        time_list.append(0)
        pass

# Save the time list into a variable
df['Sent_at'] = time_list

# Save the resulting df in a  csv file
df.to_csv('Results.csv', index=False)
