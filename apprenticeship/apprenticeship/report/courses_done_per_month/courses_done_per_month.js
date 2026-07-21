frappe.query_reports["Courses Done per Month"] = {
	"filters": [
		{
			"fieldname": "year",
			"label": __("Year"),
			"fieldtype": "Select",
			"options": ["", "2024", "2025", "2026", "2027"]
		},
		{
			"fieldname": "course",
			"label": __("Course"),
			"fieldtype": "Link",
			"options": "Training Course"
		}
	]
};