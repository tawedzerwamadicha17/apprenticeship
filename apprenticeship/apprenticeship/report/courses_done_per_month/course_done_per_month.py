from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Courses Done per Month",
        "ref_doctype": "Trainee",
        "report_type": "Query Report",
        "query": """SELECT
                DATE_FORMAT(ca.date_attended, '%Y-%m') as "Month:Data:100",
                ca.course as "Course:Link/Training Course:220",
                COUNT(*) as "Attendees:Int:100"
            FROM `tabTrainee Course Attended` ca
            WHERE ca.date_attended IS NOT NULL
            GROUP BY DATE_FORMAT(ca.date_attended, '%Y-%m'), ca.course
            ORDER BY Month DESC""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())