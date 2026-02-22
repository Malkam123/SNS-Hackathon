import streamlit as st
from workflow import graph
import tempfile
import os

st.title("📄 AI Invoice Automation Dashboard - Auto Gen AI")

# ------------------ MANUAL UPLOAD ------------------

uploaded_file = st.file_uploader("Upload Invoice (PDF)", type=["pdf"])

if uploaded_file:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    with st.spinner("Processing Invoice..."):
        result = graph.invoke({
            "file_path": temp_path,
            "invoice_data": {},
            "po_status": {},
            "erp_status": {}
        })

    invoice = result.get("invoice_data", {})
    po_status = result.get("po_status", {})
    erp_status = result.get("erp_status", {})

    st.success("Processing Complete")

    st.subheader("📄 Extracted Details")
    st.write("Invoice Number:", invoice.get("invoice_number"))
    st.write("Vendor:", invoice.get("vendor"))
    st.write("Amount:", invoice.get("amount"))
    st.write("PO Number:", invoice.get("po_number"))

    st.subheader("📊 PO Validation")
    st.write("PO Match:", po_status.get("po_match"))
    st.write("PO Status:", po_status.get("status"))

    st.subheader("🏢 ERP Status")
    st.write("ERP ID:", erp_status.get("erp_id"))
    st.write("ERP Status:", erp_status.get("erp_status"))

# ------------------ EMAIL CHECK BUTTON ------------------

if st.button("📧 Check Email for Invoices"):

    with st.spinner("Scanning inbox..."):
        result = graph.invoke({
            "file_path": "",
            "invoice_data": {},
            "po_status": {},
            "erp_status": {}
        })

    invoice = result.get("invoice_data", {})
    po_status = result.get("po_status", {})
    erp_status = result.get("erp_status", {})

    st.success("Invoice processed successfully!")

    st.subheader("📄 Extracted Details")
    st.write("Invoice Number:", invoice.get("invoice_number"))
    st.write("Vendor:", invoice.get("vendor"))
    st.write("Amount:", invoice.get("amount"))
    st.write("PO Number:", invoice.get("po_number"))

    st.subheader("📊 PO Validation")
    st.write("PO Match:", po_status.get("po_match"))
    st.write("PO Status:", po_status.get("status"))

    st.subheader("🏢 ERP Status")
    st.write("ERP ID:", erp_status.get("erp_id"))
    st.write("ERP Status:", erp_status.get("erp_status"))