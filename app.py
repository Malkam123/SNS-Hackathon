import streamlit as st
import requests

st.title("📄 AI Invoice Automation Dashboard- Auto Gen AI")

# ------------------ MANUAL UPLOAD ------------------

uploaded_file = st.file_uploader("Upload Invoice (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing Invoice..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/process-invoice", files=files)

        if response.status_code == 200:
            result = response.json()
        else:
            st.error("Backend Error")
            st.write(response.text)
            st.stop()

    st.success("Processing Complete")

    st.subheader("Extracted Details")
    st.write("Invoice Number:", result.get("invoice_data", {}).get("invoice_number"))
    st.write("Vendor:", result.get("invoice_data", {}).get("vendor"))
    st.write("Amount:", result.get("invoice_data", {}).get("amount"))
    st.write("PO Status:", result.get("po_status"))
    st.write("ERP Status:", result.get("erp_status"))

# ------------------ EMAIL CHECK BUTTON ------------------

st.divider()

if st.button("📧 Check Email for Invoices"):

    with st.spinner("Scanning inbox..."):
        response = requests.get("http://127.0.0.1:8000/process-emails")

    if response.status_code == 200:

        result = response.json()

        invoice = result.get("invoice_data", {})
        po_status = result.get("po_status", {})
        erp_status = result.get("erp_status", {})

        st.success("Invoice found and processed!")

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

    else:
        st.error("Backend Error")
        st.write(response.text)