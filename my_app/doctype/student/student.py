# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
from datetime import datetime

class student(Document):
	pass
	def validate(self):
		self.full_name = f'{self.first_name} {self.middel_name or ""} {self.last_name or ""}'
		if(self.date_of_birth):
			today = datetime.today()
			dob = datetime.strptime(self.date_of_birth,"%Y-%m-%d")
			if(today< dob):
				frappe.throw("dob error")

		

@ frappe.whitelist()
def get_address(address):
	default_address = frappe.get_doc('Address', address)
	if default_address:
		return default_address
		
