frappe.query_reports["Trainee Date of Joining or Leaving"] = {
	"filters": [
		{
			"fieldname": "dealer",
			"label": __("Dealer"),
			"fieldtype": "Link",
			"options": "Dealer"
		},
		{
			"fieldname": "engagement_from",
			"label": __("Engagement From"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "engagement_to",
			"label": __("Engagement To"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "resignation_from",
			"label": __("Resignation From"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "resignation_to",
			"label": __("Resignation To"),
			"fieldtype": "Date"
		}
	]
};