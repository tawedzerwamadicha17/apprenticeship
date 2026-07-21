frappe.query_reports["Dealer Course Participation"] = {
	"filters": [
		{
			"fieldname": "dealer",
			"label": __("Dealer"),
			"fieldtype": "Link",
			"options": "Dealer"
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