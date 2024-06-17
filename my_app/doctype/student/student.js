// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

frappe.ui.form.on("student", {
    // last_name(frm) {
    //     update_full_name(frm);
    // },
    refresh(frm) {
        var currentDate = new Date();
        var day = currentDate.getDate();
        var month = currentDate.getMonth() + 1;
        var year = currentDate.getFullYear();
        var formattedDate = year + '-' + month + '-' + day;
        frm.set_value("joining_date", formattedDate)
        if (!frm.is_new()) {
        frappe.call({
            method:'my_app.my_app.doctype.student.student.get_address',
            args:{
                address:frm.doc.address
            },
            callback: function (res){
                    address = res.message
                    formatted_address = `<div style='padding:5px;line-height:8px;border: 1px solid black; border-radius: 5px;background-color:#f3f3f3;'><h4>Address:</h4><p>${address.address_title}</p><p>${address.address_line1},${address.address_line2}</p><p>${address.city},${address.pincode}</p><p>${address.county},${address.country}</p></div>`
                    frm.fields_dict["your_address"].html(formatted_address)
            }
    })
}
        // frm.fields_dict.your_address.$wrapper.html("<h1>myData</h1>");
        frm.add_custom_button('Create User', () => {
            create_user(frm);
          
        })

    },
    
    
    
   

});

function create_user(frm){
    frappe.new_doc('User', {
        email: frm.doc.email,
        role_profile_name:"Student",
        first_name: frm.doc.first_name
    })
}


// frappe.listview_settings['student'] = {
//     onload: function(listview) {
//         listview.page.add_inner_button('Add Student', function() {
//             frappe.new_doc('Student');
//         }, 'Create');
//     }
// };