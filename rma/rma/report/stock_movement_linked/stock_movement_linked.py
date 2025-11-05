import frappe

def execute(filters=None):
    columns = ["Stock Entry:Link/Stock Entry:200","Item:Link/Item:120","Serial:Data:120","Warehouse:Link/Warehouse:200","Date:Date:120"]
    data = frappe.db.sql("""
        select sle.voucher_no, sle.item_code, sle.serial_no, sle.warehouse, sle.posting_date
        from `tabStock Ledger Entry` sle
        where sle.voucher_type = \'Stock Entry\' and sle.voucher_no like \'RMA-%\'
        order by sle.posting_date desc
    """, as_dict=True)
    rows = []
    for r in data:
        rows.append([r.voucher_no, r.item_code, r.serial_no, r.warehouse, r.posting_date])
    return columns, rows
