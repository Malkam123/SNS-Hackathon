import json

class MatchingAgent:
    def __init__(self):
        with open("data/erp_po.json") as f:
            self.po_data = json.load(f)

    def run(self, invoice):
        for po in self.po_data:
            if po["po_number"] == invoice.get("po_number"):
                return po
        return None
