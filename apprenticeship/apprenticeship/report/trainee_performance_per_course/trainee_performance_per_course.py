from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Trainee Performance per Course",
        "ref_doctype": "Trainee",
        "report_type": "Query Report",
        "query": """SELECT
                ca.parent as "Trainee:Link/Trainee:150",
                ca.course as "Course:Link/Training Course:220",
                ca.mark_obtained as "Mark Obtained:Float:110",
                ca.outcome as "Outcome:Data:90",
                ca.date_attended as "Date Attended:Date:120"
            FROM `tabTrainee Course Attended` ca
            ORDER BY ca.parent""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())