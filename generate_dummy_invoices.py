from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import zipfile
from datetime import datetime
import random

# Folder setup
output_folder = "data/invoices"
os.makedirs(output_folder, exist_ok=True)

# Dummy invoice data
invoices = [
    {
        "invoice_number": "INV-1001",
        "vendor": "ABC Supplies Ltd",
        "amount": 48250,
        "po_number": "PO-7781"
    },
    {
        "invoice_number": "INV-1002",
        "vendor": "TechNova Solutions",
        "amount": 15780,
        "po_number": "PO-8892"
    },
    {
        "invoice_number": "INV-1003",
        "vendor": "Global Industrial Corp",
        "amount": 73200,
        "po_number": "PO-9903"
    }
]

def create_invoice_pdf(data):
    file_path = os.path.join(output_folder, f"{data['invoice_number']}.pdf")
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, height - 80, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 120, f"Invoice Number: {data['invoice_number']}")
    c.drawString(50, height - 140, f"Vendor: {data['vendor']}")
    c.drawString(50, height - 160, f"PO Number: {data['po_number']}")
    c.drawString(50, height - 180, f"Invoice Date: {datetime.now().date()}")
    c.drawString(50, height - 200, "Payment Terms: Net 30")

    c.drawString(50, height - 240, f"Total Amount: ${data['amount']:,}")

    c.drawString(50, height - 280, "Thank you for your business.")

    c.save()
    return file_path


# Generate PDFs
generated_files = []
for invoice in invoices:
    generated_files.append(create_invoice_pdf(invoice))

# Create ZIP file
zip_filename = "sample_invoices.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in generated_files:
        zipf.write(file, os.path.basename(file))

print("✅ Sample invoices generated!")
print("📦 ZIP file created:", zip_filename)