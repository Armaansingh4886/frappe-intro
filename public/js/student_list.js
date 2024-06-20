frappe.listview_settings['student'] = {
    refresh: function(listview) {
        listview.page.add_menu_item(__('Custom Button'), function() {
            frappe.msgprint('Custom Button Clicked!');
        });
    }
};