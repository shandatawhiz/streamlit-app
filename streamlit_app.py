import streamlit as st
from datetime import datetime

vendors = []
invoices = []
quotations = []

def add_vendor(name, contact):
    vendor = {
        "id": len(vendors) + 1,
        "name": name,
        "contact": contact,
        "created_at": str(datetime.now())
    }
    vendors.append(vendor)
    return f"Vendor {name} added successfully."

def list_vendors():
    return vendors

def create_invoice(vendor_id, amount):
    invoice = {
        "id": len(invoices) + 1,
        "vendor_id": vendor_id,
        "amount": amount,
        "date": str(datetime.now())
    }
    invoices.append(invoice)
    return f"Invoice created for vendor ID {vendor_id}."

def list_invoices():
    return invoices

def generate_quotation(vendor_id, amount):
    quotation = {
        "id": len(quotations) + 1,
        "vendor_id": vendor_id,
        "amount": amount,
        "date": str(datetime.now())
    }
    quotations.append(quotation)
    return f"Quotation generated for vendor ID {vendor_id}."

def list_quotations():
    return quotations

st.title("Vendor and Invoice Management System")

# Vendor Management
st.header("Vendor Management")
vendor_name = st.text_input("Vendor Name")
vendor_contact = st.text_input("Vendor Contact")

if st.button("Add Vendor"):
    result = add_vendor(vendor_name, vendor_contact)
    st.success(result)

if st.button("List Vendors"):
    st.write(list_vendors())

# Invoice Management
st.header("Invoice Management")
vendor_id_invoice = st.number_input("Vendor ID for Invoice", min_value=1)
invoice_amount = st.number_input("Invoice Amount", min_value=0.0)

if st.button("Create Invoice"):
    result = create_invoice(vendor_id_invoice, invoice_amount)
    st.success(result)

if st.button("List Invoices"):
    st.write(list_invoices())

# Quotation Generation
st.header("Quotation Generator")
vendor_id_quotation = st.number_input("Vendor ID for Quotation", min_value=1)
quotation_amount = st.number_input("Quotation Amount", min_value=0.0)

if st.button("Generate Quotation"):
    result = generate_quotation(vendor_id_quotation, quotation_amount)
    st.success(result)

if st.button("List Quotations"):
    st.write(list_quotations())

    