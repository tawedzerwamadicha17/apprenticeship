from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Courses Done by Dealer",
        "ref_doctype": "Trainee",
        "report_type": "Query Report",
        "query": """SELECT
                tr.dealer as "Dealer:Link/Dealer:150",
                ca.course as "Course:Link/Training Course:220",
                COUNT(DISTINCT ca.parent) as "Trainees Attended:Int:120"
            FROM `tabTrainee Course Attended` ca
            INNER JOIN `tabTrainee` tr ON tr.name = ca.parent
            GROUP BY tr.dealer, ca.course
            ORDER BY tr.dealer, ca.course""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())