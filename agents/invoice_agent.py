import pdfplumber

class InvoiceAgent:

    def process_invoice(self, file_path: str):
        try:
            # Extract text from PDF
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()

            # 🔹 Dummy extraction logic (you can improve later)
            invoice_number = "Not Found"
            vendor = "Unknown Vendor"
            amount = "0"
            status = "Approved"

            if "Invoice" in text:
                invoice_number = "INV-001"

            if "Total" in text:
                amount = "15000"

            return {
                "invoice_number": invoice_number,
                "vendor": vendor,
                "amount": amount,
                "status": status
            }

        except Exception as e:
            return {"error": str(e)}
