import frappe
from frappe.model.document import Document

class RMAEditRequest(Document):
    def on_submit(self):
        # notify approver in-app (UI notification could be improved)
        frappe.msgprint("Edit request submitted. Approver: {0}".format(self.approver))

    def approve(self):
        # Only CEO/Admin should call approve via permissions; apply requested change
        rma = frappe.get_doc("RMA Request", self.rma_reference)
        # simple apply - expects field names to match property names
        try:
            setattr(rma, self.field_to_change, self.new_value)
            rma.flags.ignore_permissions = True
            rma.save()
            self.status = "Approved"
            self.save()
            frappe.db.commit()
        except Exception as e:
            frappe.throw("Failed to apply edit: " + str(e))
