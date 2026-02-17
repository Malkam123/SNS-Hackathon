from imapclient import IMAPClient
import email
import os
from dotenv import load_dotenv

load_dotenv()

class EmailAgent:
    def __init__(self):
        self.server = "imap.gmail.com"
        self.username = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASS")

    def fetch_unread_attachments(self):
        attachments = []

        with IMAPClient(self.server) as client:
            client.login(self.username, self.password)
            client.select_folder("INBOX")

            messages = client.search(["UNSEEN"])

            for uid, message_data in client.fetch(messages, "RFC822").items():
                msg = email.message_from_bytes(message_data[b"RFC822"])

                for part in msg.walk():
                    if part.get_content_disposition() == "attachment":
                        filename = part.get_filename()
                        file_bytes = part.get_payload(decode=True)
                        attachments.append((filename, file_bytes))

        return attachments
