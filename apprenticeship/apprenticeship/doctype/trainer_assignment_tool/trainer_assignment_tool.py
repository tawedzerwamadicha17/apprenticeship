# Copyright (c) 2026, Gabriel Real Estate (Pvt) Ltd
# License: MIT

import frappe
from frappe import _
from frappe.model.document import Document


class TrainerAssignmentTool(Document):
	@frappe.whitelist()
	def get_students(self):
		self.set("students", [])

		if self.get_students_from == "Student Group":
			if not self.student_group:
				frappe.throw(_("Please select a Cohort (Student Group)"))
			rows = frappe.get_all(
				"Student Group Student",
				filters={"parent": self.student_group, "active": 1},
				fields=["student", "student_name"],
			)
		elif self.get_students_from == "Program Enrollment":
			if not self.program:
				frappe.throw(_("Please select an Apprenticeship Programme"))
			rows = frappe.get_all(
				"Program Enrollment",
				filters={"program": self.program},
				fields=["student", "student_name"],
			)
		else:
			frappe.throw(_("Please select where to get apprentices from"))

		# de-duplicate (a student can appear more than once, e.g. multiple enrollments)
		seen = set()
		existing_active = set(
			r.student
			for r in frappe.get_all(
				"Trainer Assignment",
				filters={"instructor": self.instructor, "workplace": self.workplace, "status": "Active"},
				fields=["student"],
			)
		)

		for row in rows:
			if row.student in seen:
				continue
			seen.add(row.student)
			self.append(
				"students",
				{
					"student": row.student,
					"student_name": row.student_name,
					"already_assigned": 1 if row.student in existing_active else 0,
				},
			)

		if not self.students:
			frappe.msgprint(_("No apprentices found for the selected criteria."))

	@frappe.whitelist()
	def assign_students(self):
		if not self.students:
			frappe.throw(_("No apprentices in the list. Click 'Get Apprentices' first."))
		if not self.instructor or not self.workplace or not self.start_date:
			frappe.throw(_("Trainer / Assessor, Workplace, and Start Date are all required."))

		created = []
		skipped = []

		for row in self.students:
			if row.already_assigned:
				skipped.append(row.student_name or row.student)
				continue

			ta = frappe.get_doc(
				{
					"doctype": "Trainer Assignment",
					"student": row.student,
					"instructor": self.instructor,
					"workplace": self.workplace,
					"start_date": self.start_date,
					"end_date": self.end_date,
					"status": "Active",
				}
			)
			ta.insert(ignore_permissions=False)
			created.append(ta.name)

		frappe.msgprint(
			_("Created {0} Trainer Assignment record(s).{1}").format(
				len(created),
				(
					"<br>Skipped (already had an active assignment with this trainer/workplace): "
					+ ", ".join(skipped)
					if skipped
					else ""
				),
			)
		)
		return {"created": created, "skipped": skipped}
