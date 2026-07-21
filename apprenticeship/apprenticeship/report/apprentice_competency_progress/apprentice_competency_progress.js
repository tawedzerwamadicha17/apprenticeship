// Copyright (c) 2026, Gabriel Real Estate (Pvt) Ltd
// License: MIT

frappe.query_reports["Apprentice Competency Progress"] = {
	filters: [
		{
			fieldname: "student",
			label: __("Apprentice"),
			fieldtype: "Link",
			options: "Student",
		},
		{
			fieldname: "course",
			label: __("Training Module"),
			fieldtype: "Link",
			options: "Course",
		},
	],
};
