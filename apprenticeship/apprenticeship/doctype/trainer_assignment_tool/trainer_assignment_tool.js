// Copyright (c) 2026, Gabriel Real Estate (Pvt) Ltd
// License: MIT

frappe.ui.form.on("Trainer Assignment Tool", {
	refresh: function (frm) {
		frm.disable_save();

		frm.add_custom_button(__("Get Apprentices"), function () {
			frm.call("get_students").then(() => {
				frm.refresh_field("students");
				frm.refresh();
			});
		}).addClass("btn-primary");

		if (frm.doc.students && frm.doc.students.length) {
			frm.add_custom_button(__("Create Trainer Assignments"), function () {
				frappe.confirm(
					__("This will create a Trainer Assignment record for every apprentice listed below (skipping any that already have an active assignment with this trainer/workplace). Continue?"),
					() => {
						frm.call("assign_students").then(() => {
							frm.reload_doc();
						});
					}
				);
			}).addClass("btn-primary");
		}
	},

	get_students_from: function (frm) {
		frm.set_value("students", []);
	},
});
