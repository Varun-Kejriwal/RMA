frappe.ui.form.on("RMA Request", {
    serial_number: function(frm) {
        if (!frm.doc.serial_number) return;
        frappe.call({
            method: "rma.rma.doctype.rma_request.rma_request_server.get_serial_details",
            args: { serial_no: frm.doc.serial_number },
            callback: function(r) {
                if (r.message) {
                    frm.set_value("item_name", r.message.item_name);
                    frm.set_value("customer", r.message.customer);
                    frm.set_value("date_of_sale", r.message.date_of_sale);
                    frm.set_value("warranty_expiry_date", r.message.warranty_expiry_date);
                    frm.set_value("warranty_status", r.message.warranty_status);
                } else {
                    frappe.msgprint("No sale/serial info found for this serial number.");
                }
            }
        });
    },
    action: function(frm) {
        if (frm.doc.action == "Replace") {
            frm.set_df_property("new_serial_number", "reqd", true);
        } else {
            frm.set_df_property("new_serial_number", "reqd", false);
        }
    },
    onload: function(frm) {
        // UI nicety; server enforces permissions
    }
});
