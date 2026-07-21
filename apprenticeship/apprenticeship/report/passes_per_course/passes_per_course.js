frappe.query_reports["Passes per Course"] = {
	"filters": [
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