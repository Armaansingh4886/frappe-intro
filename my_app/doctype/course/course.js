// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

frappe.ui.form.on("Course", {
	refresh(frm) {
                frappe.call({
                        method:'my_app.my_app.doctype.course.course.get_all_courses',
                        callback: function (res){
                                console.log(res);
                        }
                })
        
	},
});


