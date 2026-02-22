import os

class EmailAgent:
    """
    Simulated Email Agent for Hackathon Demo
    Instead of connecting to Gmail,
    it scans a local folder for invoice PDFs.
    """

    def __init__(self, folder_path="data/invoices"):
        self.folder_path = folder_path

    def fetch_invoice_attachments(self):
        if not os.path.exists(self.folder_path):
            return []

        files = []

        for file in os.listdir(self.folder_path):
            if file.endswith(".pdf"):
                files.append(os.path.join(self.folder_path, file))

        return files