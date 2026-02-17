import streamlit as st
import requests

st.set_page_config(page_title="Invoice Automation", layout="centered")

st.title("📧 Email to ERP Invoice Automation")

backend_url = "http://127.0.0.1:8000"

# -------- OPTION 1: Process Email --------
st.subheader("Process Invoices from Email")

if st.button("Fetch & Process Emails"):
    with st.spinner("Processing emails..."):
        response = requests.get(f"{backend_url}/process-emails")

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            if results:
                for invoice in results:
                    st.success("Invoice Processed ✅")

                    st.write("Invoice Number:", invoice.get("invoice_number"))
                    st.write("Vendor:", invoice.get("vendor"))
                    st.write("Amount:", invoice.get("amount"))
                    st.write("Status:", invoice.get("status"))
                    st.divider()
            else:
                st.warning("No invoices found.")
        else:
            st.error("Error processing emails")


# -------- OPTION 2: Manual Upload --------
st.subheader("Upload Invoice Manually")

uploaded_file = st.file_uploader("Drag & Drop Invoice PDF", type=["pdf"])

if uploaded_file:
    if st.button("Process Uploaded Invoice"):
        with st.spinner("Processing invoice..."):

            files = {"file": uploaded_file.getvalue()}
            response = requests.post(
                f"{backend_url}/process-invoice",
                files={"file": uploaded_file}
            )

            if response.status_code == 200:
                invoice = response.json()

                st.success("Invoice Processed ✅")

                st.write("Invoice Number:", invoice.get("invoice_number"))
                st.write("Vendor:", invoice.get("vendor"))
                st.write("Amount:", invoice.get("amount"))
                st.write("Status:", invoice.get("status"))

            else:
                st.error("Processing failed")


# -------- LOGS SECTION --------
st.subheader("Logs")

if st.button("Check Backend Health"):
    try:
        r = requests.get(f"{backend_url}/docs")
        if r.status_code == 200:
            st.success("Backend is running ✅")
    except:
        st.error("Backend not running ❌")
