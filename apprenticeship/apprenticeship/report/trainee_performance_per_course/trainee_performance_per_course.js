frappe.query_reports["Trainee Performance per Course"] = {
	"filters": [
		{
			"fieldname": "trainee",
			"label": __("Trainee"),
			"fieldtype": "Link",
			"options": "Trainee"
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
		},
		{
			"fieldname": "outcome",
			"label": __("Outcome"),
			"fieldtype": "Select",
			"options": ["", "Pass", "Fail"]
		}
	]
};