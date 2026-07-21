# Copyright (c) 2026, Gabriel Real Estate (Pvt) Ltd
# License: MIT

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime


class PracticalAssessment(Document):
	def validate(self):
		# Stamp sign-off timestamps automatically when the checkboxes are ticked
		if self.assessor_signed and not self.assessor_signed_on:
			self.assessor_signed_on = now_datetime()
		if self.apprentice_signed and not self.apprentice_signed_on:
			self.apprentice_signed_on = now_datetime()

		if self.outcome == "Competent" and not self.evidence:
			frappe.msgprint(
				"Consider attaching photo/video evidence to support a 'Competent' outcome.",
				alert=True,
				indicator="orange",
			)

	def before_submit(self):
		if not self.assessor_signed:
			frappe.throw("The Assessor must confirm the outcome (tick 'Assessor Confirms Outcome') before submitting.")
