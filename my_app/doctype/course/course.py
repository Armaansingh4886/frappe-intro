# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Course(Document):
	pass

@frappe.whitelist()
def get_all_courses():
	all_data=[]
	courses = frappe.get_all("Course", fields=['name','course_name','course_code','credits','acedemic_year','topics'])
	for course in courses:
		all_data.append(	frappe.get_doc("Course",course))
	
	return all_data


def add_course(course):
	if(not course.name or not course.code or  not course.credits or not course.acedemic_year or not course.topics):
		frappe.throw("Enter all fields")
		return
	doc = frappe.get_doc(doctype="Course",course_name=course.name or"",course_code=course.code or"",credits=course.credits or "", acedemic_year = course.acedemic_year or "",topics=course.topics or "")
	doc.insert()
	frappe.db.commit()
	return "course successfuly added"


def delete_course(name):
	frappe.delete_doc("Course",name)
	frappe.db.commit()
	return "course successfuly deleted"

def update_course(data):
	doc = frappe.get_doc("Course", data.name)
        
	for key, value in data.items():
		if hasattr(doc, key):
			setattr(doc, key, value)
        
	doc.save()
	frappe.db.commit()  


	

