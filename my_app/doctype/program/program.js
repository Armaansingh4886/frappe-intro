// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

frappe.ui.form.on("Program", {
	refresh(frm) {
        
        
	},
	start_date(frm){
		check_date(frm)
	},
	end_date(frm){
		check_date(frm)
	}
});

function check_date(frm){
	sDate =frm.doc.start_date
	eDate =frm.doc.end_date
	console.log(eDate-sDate);
}