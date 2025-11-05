import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def get_serial_details(serial_no):
    # Minimal fetch: retrieve item_code and warranty expiry from Serial No master
    serial = frappe.db.get_value("Serial No", serial_no, ["item_code","warranty_expiry_date"], as_dict=True)
    if not serial:
        return None
    item_code = serial.get("item_code")
    warranty_expiry_date = serial.get("warranty_expiry_date")
    # attempt to find a linked Sales Invoice posting date and customer
    sale = frappe.db.sql("""
        SELECT si.customer, si.posting_date
        FROM `tabSales Invoice Item` sii
        JOIN `tabSales Invoice` si ON si.name = sii.parent
        WHERE sii.serial_no LIKE CONCAT('%', %s, '%')
        LIMIT 1
    """, (serial_no,), as_dict=True)
    customer = None
    date_of_sale = None
    if sale:
        customer = sale[0].get("customer")
        date_of_sale = sale[0].get("posting_date")
    status = "Expired"
    if warranty_expiry_date and nowdate() <= warranty_expiry_date:
        status = "Available"
    return {
        "item_name": item_code,
        "customer": customer,
        "date_of_sale": date_of_sale,
        "warranty_expiry_date": warranty_expiry_date,
        "warranty_status": status
    }
