# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class test(Document):
	pass

class test(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.hidden = f'{self.f_name} {self.hidden or ""}'

