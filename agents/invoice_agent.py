import pdfplumber

class InvoiceAgent:

    def process_invoice(self, file_path: str):
        try:
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
                    print("------ RAW PDF TEXT ------")
                    print(text)
                    print("--------------------------")
            invoice_data = {
                "invoice_number": self.get_value(text, "Invoice Number"),
                "vendor": self.get_value(text, "Vendor"),
                "amount": self.get_value(text, "Total Amount"),
                "po_number": self.get_value(text, "PO Number"),
                "status": "Processed"
            }

            return invoice_data

        except Exception as e:
            return {"error": str(e)}

    def get_value(self, text, field_name):
        for line in text.split("\n"):
            if field_name.lower() in line.lower():
                parts = line.split(":")
                if len(parts) > 1:
                    return parts[1].strip()
        return None