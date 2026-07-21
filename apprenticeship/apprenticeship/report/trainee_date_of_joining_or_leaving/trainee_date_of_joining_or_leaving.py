from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Trainee Date of Joining or Leaving",
        "ref_doctype": "Trainee",
        "report_type": "Query Report",
        "query": """SELECT
                name as "Trainee:Link/Trainee:150",
                full_name as "Trainee Name:Data:180",
                date_of_engagement as "Date of Engagement:Date:130",
                date_of_resignation as "Date of Resignation:Date:130",
                dealer as "Dealer:Link/Dealer:150"
            FROM `tabTrainee`
            ORDER BY date_of_engagement DESC""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())