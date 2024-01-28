import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

def send_email(email_sender, email_password, email_receiver, subject, body, attachment_file_name):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Make the message multipart
    em.add_alternative(body, subtype='html')

    # Attach the file
    with open(attachment_file_name, 'rb') as attachment_file:
        file_data = attachment_file.read()
        file_name = os.path.basename(attachment_file_name)

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    em.attach(attachment)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def main():
    try:
        # User Inputs
        email_sender = input("Enter your email: ")
        email_password = input("Enter your email password: ")  # Prompt for password
        subject = input("Enter the email subject: ")
        body = input("Enter the email body: ")
        attachment_file_path = input("Enter the full path of the attachment file: ")
        csv_path = input("Enter the CSV file path: ")

        # Reading the CSV file
        emails_df = pd.read_csv(csv_path)

        # Looping through the CSV file and sending emails with attachments
        for index, row in emails_df.iterrows():
            email_receiver = row['Receiver']
            send_email(email_sender, email_password, email_receiver, subject, body, attachment_file_path)

        print("Emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
