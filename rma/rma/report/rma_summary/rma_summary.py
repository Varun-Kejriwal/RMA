import frappe

def execute(filters=None):
    columns = ["RMA:Link/RMA Request:150","Serial:Data:150","Customer:Link/Customer:150","Action:Data:80","Status:Data:100","Date:Date:120"]
    data = frappe.db.sql("""
        select name, serial_number, customer, action, system_status, replacement_date
        from `tabRMA Request` order by creation desc
    """, as_dict=True)
    rows = []
    for r in data:
        rows.append([r.name, r.serial_number, r.customer, r.action, r.system_status, r.replacement_date])
    return columns, rows
