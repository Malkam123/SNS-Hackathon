from langgraph.graph import StateGraph
from typing import TypedDict
from agents.invoice_agent import InvoiceAgent
from agents.po_agent import POAgent
from agents.erp_agent import ERPAgent
from agents.email_agent import EmailAgent
import os
from dotenv import load_dotenv

load_dotenv()


class InvoiceState(TypedDict):
    file_path: str
    invoice_data: dict
    po_status: dict
    erp_status: dict

invoice_agent = InvoiceAgent()
po_agent = POAgent()
erp_agent = ERPAgent()
email_agent = EmailAgent()


def extract_invoice(state: InvoiceState):
    state["invoice_data"] = invoice_agent.process_invoice(state["file_path"])
    return state

def validate_po(state: InvoiceState):
    state["po_status"] = po_agent.validate_invoice(state["invoice_data"])
    return state

def push_to_erp(state: InvoiceState):
    state["erp_status"] = erp_agent.create_entry(state["invoice_data"])
    return state

def email_node(state: InvoiceState):
    files = email_agent.fetch_invoice_attachments()

    if not files:
        state["invoice_data"] = {"error": "No invoices found in email simulation"}
        return state

    # Take first invoice for demo
    state["file_path"] = files[0]

    return state


builder = StateGraph(InvoiceState)

builder.add_node("extract", extract_invoice)
builder.add_node("validate_po", validate_po)
builder.add_node("erp", push_to_erp)
builder.add_node("email_scan", email_node)

builder.set_entry_point("email_scan")
builder.add_edge("email_scan", "extract")
builder.add_edge("extract", "validate_po")
builder.add_edge("validate_po", "erp")

graph = builder.compile()
