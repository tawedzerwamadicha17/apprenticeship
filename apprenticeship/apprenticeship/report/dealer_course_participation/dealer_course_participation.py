from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Dealer Course Participation",
        "ref_doctype": "Dealer",
        "report_type": "Query Report",
        "query": """SELECT
                tr.dealer as "Dealer:Link/Dealer:150",
                COUNT(DISTINCT tr.name) as "Trainees:Int:100",
                COUNT(ca.name) as "Course Attendances:Int:150"
            FROM `tabTrainee` tr
            LEFT JOIN `tabTrainee Course Attended` ca ON ca.parent = tr.name
            GROUP BY tr.dealer
            ORDER BY tr.dealer""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())