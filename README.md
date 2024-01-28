**Email Sender with Attachment - README**

This Python script allows you to send emails with attachments to multiple recipients using a CSV file as a data source. Below are the instructions and details for using the script:

### Features:
- Send emails with attachments to multiple recipients.
- User-friendly prompts for email details and CSV file path.
- Dynamically prompts for email password during runtime.
- Handles exceptions and provides success messages.

### Prerequisites:
- Python installed on your system.
- Gmail account for sending emails.
- Allow access for "Less secure app access" in your Gmail account settings or use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) if two-factor authentication is enabled.

### Usage Instructions:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/TUR14CUS/Email-Sender.git
   cd Email-Sender
   ```

2. **Install Dependencies:**
   ```bash
   pip install pandas
   ```

3. **Run the Script:**
   ```bash
   python email_sender.py
   ```

4. **Enter Email Details:**
   - Enter your email address, password, subject, body, attachment file path, and CSV file path when prompted.

5. **Review Email Content:**
   - Review the CSV file format with columns `Receiver` and `Attachment`.

6. **Email Sending:**
   - The script will send emails with attachments to the specified recipients using the details provided.

### Note:
- Ensure the CSV file contains valid email addresses under the `Receiver` column and valid file paths under the `Attachment` column.

- Consider using app-specific passwords or OAuth tokens for enhanced security rather than entering your main email password directly.

- The script uses the Gmail SMTP server. If you're using a different email provider, you may need to adjust the SMTP server details in the script.

Feel free to reach out for any assistance or feedback!
