from openai import OpenAI
import pdfplumber
import io
import json

class ExtractionAgent:
    def __init__(self):
        self.client = OpenAI()

    def run(self, pdf_bytes):
        text = ""

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        prompt = f"""
        Extract:
        vendor_name
        invoice_number
        po_number
        amount
        invoice_date

        Return STRICT JSON.

        Invoice:
        {text}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You extract structured invoice data."},
                {"role": "user", "content": prompt}
            ]
        )

        return json.loads(response.choices[0].message.content)
