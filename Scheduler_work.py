import frappe

def increaseValue():
    doc = frappe.get_doc('scheduler working')
    doc.value = int(doc.value)+1
    doc.save()
    frappe.db.commit()
    return doc.value
