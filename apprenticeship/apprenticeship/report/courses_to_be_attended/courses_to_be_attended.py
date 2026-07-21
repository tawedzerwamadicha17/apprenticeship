from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Courses to be Attended",
        "ref_doctype": "Trainee",
        "report_type": "Query Report",
        "query": """SELECT
                cta.parent as "Trainee:Link/Trainee:150",
                cta.course as "Course:Link/Training Course:220",
                cta.planned_date as "Planned Date:Date:120"
            FROM `tabTrainee Course To Attend` cta
            ORDER BY cta.planned_date""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())