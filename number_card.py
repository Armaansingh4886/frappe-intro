import frappe

@frappe.whitelist()
def count_user():
    return frappe.db.sql("""SELECT count(*) from tabUser""")[0][0]