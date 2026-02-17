class DecisionAgent:
    def run(self, invoice, po):
        if not po:
            return "Rejected", "PO not found"

        invoice_amount = float(invoice.get("amount", 0))
        po_amount = float(po.get("amount", 0))

        if abs(invoice_amount - po_amount) < 5:
            return "Approved", "Amount matched"

        return "Flagged", "Amount mismatch"
