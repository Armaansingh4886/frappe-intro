# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Program(Document):
	def validate(self):
		
		total_credits =0
		for course in self.courses:
			credit = frappe.get_doc("Course",course).credits
			total_credits = total_credits+credit
			print(total_credits)
		self.total_credits= total_credits

		if(not self.start_date<self.end_date):
			frappe.throw("Make sure end date is after start date")
		else:
			sDate = datetime.strptime(self.start_date,'%Y-%m-%d')
			eDate = datetime.strptime(self.end_date,'%Y-%m-%d')
			print((eDate - sDate).days)
			self.duration=(eDate - sDate).days

