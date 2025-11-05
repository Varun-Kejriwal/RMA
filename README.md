# RMA App for ERPNext v15

A minimal functional RMA (Return Merchandise Authorization) module for ERPNext v15.

Features:
- Doctypes: RMA Request, RMA Edit Request
- Workflow: Draft -> Submitted -> Approved/Rejected -> Completed
- Warranty check from Serial No
- Repair / Replace actions
- Locked after submit
- CEO/Admin approval for edits
- Auto stock adjustment using branch-linked warehouses (requires Branch to have buffer_warehouse / damaged_warehouse fields)
