# Copyright (c) 2026, Tawe
# License: MIT

import frappe


def sync_apprentice_user_permission(doc, method=None):
	"""
	Runs on Trainee save.
	If the Trainee record has a Portal User Account (user) set, make sure that user:
	  1. has the "Apprentice" role, and
	  2. has a User Permission restricting them to their own Trainee record
	     (and, by extension, their own Practical Assessment / Trainer Assignment
	     records, since those link back to Trainee).
	"""
	if not doc.user:
		return

	try:
		user = frappe.get_doc("User", doc.user)
	except frappe.DoesNotExistError:
		frappe.log_error(
			title="Apprenticeship: user permission sync failed",
			message=f"Trainee {doc.name} has User ID '{doc.user}' set, but no matching User record exists.",
		)
		return

	user.add_roles("Apprentice")

	exists = frappe.db.exists(
		"User Permission",
		{"user": doc.user, "allow": "Trainee", "for_value": doc.name},
	)
	if not exists:
		frappe.get_doc(
			{
				"doctype": "User Permission",
				"user": doc.user,
				"allow": "Trainee",
				"for_value": doc.name,
				"apply_to_all_doctypes": 1,
			}
		).insert(ignore_permissions=True)
