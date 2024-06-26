// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

frappe.query_reports["sales order report"] = {
	"filters": [
		
				{
					fieldname: 'company',
					label: __('Company'),
					fieldtype: 'Link',
					options: 'Company',
					required:"1",
					default: frappe.defaults.get_user_default('company')
				},
				{
					fieldname: 'delivery_date',
					label: __('Delivery date before'),
					fieldtype: 'Date',
					
				}
		
		
	]
};

