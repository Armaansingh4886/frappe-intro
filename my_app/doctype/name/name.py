# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class name(Document):
	def validate(self):
		if self.set_full_name:
			self.full_name = f'{self.first_name or ""} {self.last_name or ""}'
