frappe.query_reports["Courses to be Attended"] = {
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
			"label": __("Planned From"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("Planned To"),
			"fieldtype": "Date"
		}
	]
};