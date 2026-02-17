from fastapi import FastAPI, UploadFile, File
from agents.invoice_agent import InvoiceAgent
from agents.email_agent import EmailAgent
import shutil
import os

app = FastAPI()

@app.get("/process-emails")
def process_emails():
    email_agent = EmailAgent()
    attachments = email_agent.fetch_unread_attachments()

    results = []
    invoice_agent = InvoiceAgent()

    for file_path in attachments:
        result = invoice_agent.process_invoice(file_path)
        results.append(result)

    return {"results": results}


@app.post("/process-invoice")
async def process_invoice(file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"

    os.makedirs("temp", exist_ok=True)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    invoice_agent = InvoiceAgent()
    result = invoice_agent.process_invoice(file_location)

    return result
