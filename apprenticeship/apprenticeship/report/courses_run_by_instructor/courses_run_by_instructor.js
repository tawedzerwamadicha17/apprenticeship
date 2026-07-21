frappe.query_reports["Courses Run by Instructor"] = {
	"filters": [
		{
			"fieldname": "instructor",
			"label": __("Instructor"),
			"fieldtype": "Link",
			"options": "Instructor"
		},
		{
			"fieldname": "course",
			"label": __("Course"),
			"fieldtype": "Link",
			"options": "Training Course"
		},
		{
			"fieldname": "from_date",
			"label": __("Start From"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("Start To"),
			"fieldtype": "Date"
		}
	]
};