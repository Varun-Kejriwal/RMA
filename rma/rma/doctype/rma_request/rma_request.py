# server side controller for RMA Request
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class RMARequest(Document):
    def validate(self):
        # auto-set replacement date if empty
        if not self.replacement_date:
            self.replacement_date = nowdate()

    def on_submit(self):
        # lock for staff by setting system_status and preventing edits via before_save
        self.system_status = "Submitted"
        self.approval_status = "Pending"
        frappe.db.commit()

    def on_cancel(self):
        # prevent cancel unless Admin/CEO (permission enforced externally)
        if not frappe.has_permission("RMA Request", ptype="cancel"):
            frappe.throw("Only Admin/CEO can cancel RMA requests.")
