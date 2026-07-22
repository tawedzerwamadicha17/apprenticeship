# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import create_or_update_report

def get_report_data():
    return {
        "name": "Passes per Course",
        "ref_doctype": "Training Course",
        "report_type": "Query Report",
        "query": """SELECT
                ca.course as "Course:Link/Training Course:220",
                SUM(CASE WHEN ca.outcome = 'Pass' THEN 1 ELSE 0 END) as "Passes:Int:90",
                COUNT(*) as "Total Attempts:Int:120",
                ROUND(SUM(CASE WHEN ca.outcome = 'Pass' THEN 1 ELSE 0 END) / COUNT(*) * 100, 1) as "Pass Rate %%:Float:120"
            FROM `tabTrainee Course Attended` ca
            GROUP BY ca.course""",
        "roles": [{"role": "Education Manager"}, {"role": "Instructor"}, {"role": "System Manager"}],
        "add_total_row": 0,
        "disable_prepared_report": 0,
        "prepared_report": 0,
    }

def create():
    create_or_update_report(get_report_data())
