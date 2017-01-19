'''
Created on Jan 19, 2017

@author: Anil Kumar
'''
config = {
    "host": "localhost",
    "user": "root",
    "password": "4595@blue",
    "db": "trial"
    }

filename = r'/Python_data_migrate/resources/Consumer_Complaints.csv'

seq = ['complaint_id', 'rcv_date', 'company', 'cmp_rcv_date', 'state',
       'zip_code', 'submit_mode', 'product', 'sub_product', 'issue',
       'sub_issue', 'tags', 'consent', 'con_dispute', 'con_comp_narr',
       'cmp_pub_resp', 'cmp_con_resp', 'timely_resp']

length = {
    'complaint_id': 7,
    'rcv_date': 10,
    'company': 70,
    'cmp_rcv_date': 10,
    'state': 6,
    'zip_code': 7,
    'submit_mode': 15,
    'product': 30,
    'sub_product': 40,
    'issue': 50,
    'sub_issue': 50,
    'tags': 50,
    'consent': 100,
    'con_dispute': 1,
    'con_comp_narr': 199,
    'cmp_pub_resp': 100,
    'cmp_con_resp': 40,
    'timely_resp': 1
    }

db_map = {
    'complaint_id': 'Complaint ID',
    'rcv_date': 'Date received',
    'company': 'Company',
    'cmp_rcv_date': 'Date sent to company',
    'state': 'State',
    'zip_code': 'ZIP code',
    'submit_mode': 'Submitted via',
    'product': 'Product',
    'sub_product': 'Sub-product',
    'issue': 'Issue',
    'sub_issue': 'Sub-issue',
    'tags': 'Tags',
    'consent': 'Consumer consent provided',
    'con_dispute': 'Consumer disputed',
    'con_comp_narr': 'Consumer complaint narrative',
    'cmp_pub_resp': 'Company public response',
    'cmp_con_resp': 'Company response to consumer',
    'timely_resp': 'Timely response'
    }
