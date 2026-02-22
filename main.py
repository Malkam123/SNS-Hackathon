from fastapi import FastAPI, UploadFile, File
import os
from workflow import graph

app = FastAPI()

@app.post("/process-invoice")
async def process_invoice(file: UploadFile = File(...)):

    file_location = f"temp/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    result = graph.invoke({
    "file_path": file_location,
    "invoice_data": {},
    "po_status": {},
    "erp_status": {}
})

    return result
@app.get("/process-emails")
def process_emails():
    result = graph.invoke({
        "file_path": "",
        "invoice_data": {},
        "po_status": {},
        "erp_status": {}
    })
    return result