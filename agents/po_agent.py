class POAgent:

    def validate_invoice(self, invoice_data: dict):

        # Dummy logic
        if invoice_data.get("amount") == "15000":
            return {"po_match": True, "status": "Approved"}
        else:
            return {"po_match": False, "status": "Flagged"}
