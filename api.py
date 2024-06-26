# import frappe
# @frappe.whitelist()
# def requests():
#     all_data=[]
#     courses = frappe.get_all("Course", fields=['name','course_name','course_code','credits','acedemic_year','topics'])
#     for course in courses:
#         all_data.append(	frappe.get_doc("Course",course))
	
#     return all_data


# def get_all_courses():
# 	all_data=[]
# 	courses = frappe.get_all("Course", fields=['name','course_name','course_code','credits','acedemic_year','topics'])
# 	for course in courses:
# 		all_data.append(	frappe.get_doc("Course",course))
	
# 	return all_data


# def add_course(course):
# 	if(not course.name or not course.code or  not course.credits or not course.acedemic_year or not course.topics):
# 		frappe.throw("Enter all fields")
# 		return
# 	doc = frappe.get_doc(doctype="Course",course_name=course.name or"",course_code=course.code or"",credits=course.credits or "", acedemic_year = course.acedemic_year or "",topics=course.topics or "")
# 	doc.insert()
# 	frappe.db.commit()
# 	return "course successfuly added"


# def delete_course(name):
# 	frappe.delete_doc("Course",name)
# 	frappe.db.commit()
# 	return "course successfuly deleted"

# def update_course(data):
# 	doc = frappe.get_doc("Course", data.name)
        
# 	for key, value in data.items():
# 		if hasattr(doc, key):
# 			setattr(doc, key, value)
        
# 	doc.save()
# 	frappe.db.commit()  
	




import frappe
from frappe import _


@frappe.whitelist()
def get_items():
    if(frappe.local.request.method != "GET"):
        # frappe.throw("only post request si accepted")
        return "only GET request is accepted"
    doctype = frappe.local.form_dict.get('doctype')
    name = frappe.local.form_dict.get("name")
    if not doctype:
        return {"error": "Required :- doctype "}, 400

    if(name):
        try:
            item = frappe.get_doc(doctype, name)
            return item
        except Exception as e:
            return {"error": str(e)}, 500
        
    all_items=[]
   
    try:
        records = frappe.get_all(doctype, fields=["*"])
        for record in records:
            all_items.append(frappe.get_doc(doctype,record))
        return all_items
    except Exception as e:
        return {"error": str(e)}, 500
@frappe.whitelist()
def create_item():
    if(frappe.local.request.method != "POST"):
        # frappe.throw("only post request si accepted")
        return "only POST request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    if not doctype:
        return {"error": "Required :- doctype"}, 400

    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500
@frappe.whitelist()
def update_item():
    if(frappe.local.request.method != "PUT"):
        # frappe.throw("only post request si accepted")
        return "only PUT request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "Required :- doctype and name "}, 400

    try:
        doc = frappe.get_doc(doctype, name)
        doc.update(data)
        doc.save()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500
@frappe.whitelist()
def delete_item():
    if(frappe.local.request.method != "DELETE"):
        # frappe.throw("only post request si accepted")
        return "only DELETE request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "!Required:- doctype and name"}, 400

    try:
        frappe.delete_doc(doctype, name)
        return {"message": f"Item {name} deleted successfully"}
    except Exception as e:
        return {"error": str(e)}, 500
    


@ frappe.whitelist()
def get_users():
    return frappe.get_all("User",fields=["*"])


@ frappe.whitelist()
def add_user():
    if(frappe.local.request.method != "POST"):
        # frappe.throw("only post request si accepted")
        return "only POST request is accepted"
    data = frappe.local.form_dict
    try:
        user = frappe.get_doc({"doctype":"User",**data})
        user.insert()
        frappe.db.commit()
        return user.as_dict()
    except Exception as e:
        return {"error": str(e)},500

