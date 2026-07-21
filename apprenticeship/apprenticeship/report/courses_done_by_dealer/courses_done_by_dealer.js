frappe.query_reports["Courses Done by Dealer"] = {
	"filters": [
		{
			"fieldname": "dealer",
			"label": __("Dealer"),
			"fieldtype": "Link",
			"options": "Dealer"
		},
		{
			"fieldname": "course",
			"label": __("Course"),
			"fieldtype": "Link",
			"options": "Training Course"
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		}
	]
};