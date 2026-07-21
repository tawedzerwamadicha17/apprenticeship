from . import __version__ as app_version

app_name = "apprenticeship"
app_title = "Apprenticeship"
app_publisher = "Tawe"
app_description = "Apprenticeship training and workplace assessment"
app_icon = "octicon octicon-mortar-board"
app_color = "blue"
app_email = "mtawedzerwadonald17@gmail.com"
app_license = "MIT"

# This app is self-contained: Trainee, Trainer, Training Course, Competency,
# Workplace, Dealer, Programme, and Cohort are all this app's own doctypes.
# It does not depend on the Education app.
required_apps = []

add_to_apps_screen = [
	{
		"name": "apprenticeship",
		"title": "Apprenticeship",
		"route": "/app/apprenticeship",
	}
]

# Fixtures let `bench --site your-site migrate` install/export:
# - the Translation relabeling (kept for any lingering "Student"/"Instructor"/
#   "Program"/"Course"/"Student Group" strings still shown elsewhere in the UI)
# - the Apprentice / Instructor / Education Manager roles
# - the Practical Assessment approval workflow, its portal Web Form, its
#   Notifications, its Print Format, and the Apprenticeship Workspace
fixtures = [
	{"doctype": "Role", "filters": [["role_name", "in", ["Apprentice", "Instructor", "Education Manager"]]]},
	{"doctype": "Translation", "filters": [
		["language", "=", "en"],
		["source_text", "in", [
			"Student", "Students", "Student Name",
			"Instructor", "Instructors", "Instructor Name",
			"Program", "Programs",
			"Course", "Courses",
			"Student Group", "Student Groups",
		]],
	]},
	{"doctype": "Web Form", "filters": [["name", "=", "My Practical Assessments"]]},
	{"doctype": "Workflow", "filters": [["name", "=", "Practical Assessment Workflow"]]},
	{"doctype": "Notification", "filters": [["name", "in", [
		"Practical Assessment Awaiting Review",
		"Practical Assessment Sent Back",
		"Practical Assessment Signed Off",
	]]]},
	{"doctype": "Print Format", "filters": [["name", "=", "Practical Assessment Sign-off"]]},
	{"doctype": "Workspace", "filters": [["name", "=", "Apprenticeship"]]},
]

# When a Trainee record is saved with a "Portal User Account" set, automatically
# give that user the Apprentice role and a User Permission scoping them to their
# own Trainee record (and, by extension, their own Practical Assessment /
# Trainer Assignment records, since those link back to Trainee) - this is what
# makes "apprentices log in themselves and only see their own stuff" work
# without any manual per-apprentice setup.
doc_events = {
	"Trainee": {
		"on_update": "apprenticeship.utils.sync_apprentice_user_permission",
	}
}
