# Copyright (c) 2026, Gabriel Real Estate (Pvt) Ltd
# License: MIT

import frappe
from frappe import _


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return [
		{"label": _("Apprentice"), "fieldname": "student", "fieldtype": "Link", "options": "Student", "width": 140},
		{"label": _("Apprentice Name"), "fieldname": "student_name", "fieldtype": "Data", "width": 180},
		{"label": _("Mandatory Competencies"), "fieldname": "total_mandatory", "fieldtype": "Int", "width": 160},
		{"label": _("Signed Off - Competent"), "fieldname": "completed", "fieldtype": "Int", "width": 170},
		{"label": _("Outstanding"), "fieldname": "outstanding", "fieldtype": "Int", "width": 120},
		{"label": _("% Complete"), "fieldname": "percent_complete", "fieldtype": "Percent", "width": 110},
	]


def get_data(filters):
	student_filter = filters.get("student")
	course_filter = filters.get("course")

	competency = frappe.qb.DocType("Competency")
	competency_query = frappe.qb.from_(competency).select(competency.name).where(competency.is_mandatory == 1)
	if course_filter:
		competency_query = competency_query.where(competency.course == course_filter)
	mandatory_competencies = [row.name for row in competency_query.run(as_dict=True)]

	if not mandatory_competencies:
		return []

	student = frappe.qb.DocType("Student")
	student_query = frappe.qb.from_(student).select(student.name, student.student_name)
	if student_filter:
		student_query = student_query.where(student.name == student_filter)
	students = student_query.run(as_dict=True)

	pa = frappe.qb.DocType("Practical Assessment")
	signed_off_rows = (
		frappe.qb.from_(pa)
		.select(pa.student, pa.competency)
		.where(pa.workflow_state == "Signed Off")
		.where(pa.outcome == "Competent")
		.where(pa.competency.isin(mandatory_competencies))
		.run(as_dict=True)
	)

	completed_map = {}
	for row in signed_off_rows:
		completed_map.setdefault(row.student, set()).add(row.competency)

	total_mandatory = len(mandatory_competencies)
	data = []
	for s in students:
		completed = len(completed_map.get(s.name, set()))
		outstanding = total_mandatory - completed
		percent = round((completed / total_mandatory) * 100, 1) if total_mandatory else 0
		data.append(
			{
				"student": s.name,
				"student_name": s.student_name,
				"total_mandatory": total_mandatory,
				"completed": completed,
				"outstanding": outstanding,
				"percent_complete": percent,
			}
		)

	return data
