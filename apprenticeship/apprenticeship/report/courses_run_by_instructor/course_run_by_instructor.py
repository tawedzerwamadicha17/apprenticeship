from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Courses Run by Instructor",
        "ref_doctype": "Training Course",
        "report_type": "Query Report",
        "query": """SELECT
                instructor as "Instructor:Link/Instructor:150",
                course_name as "Course:Link/Training Course:220",
                type as "Type:Data:120",
                start_date as "Start Date:Date:100",
                end_date as "End Date:Date:100"
            FROM `tabTraining Course`
            ORDER BY instructor, start_date""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())