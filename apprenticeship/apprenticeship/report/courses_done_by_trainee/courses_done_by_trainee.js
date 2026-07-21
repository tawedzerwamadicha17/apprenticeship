frappe.query_reports["Courses Done by Trainee"] = {
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
			"label": __("Attended From"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("Attended To"),
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