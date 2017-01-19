'''
Created on Jan 19, 2017

@author: Anil Kumar
'''

import setenv as se
import pymysql
import csv
from datetime import datetime as dt

conn = pymysql.connect(**(se.config))

sql = ("insert into consumer(complaint_id, rcv_date, company,"
       "cmp_rcv_date, state, zip_code, submit_mode, product,"
       "sub_product, issue, sub_issue, tags, consent, con_dispute,"
       "con_comp_narr, cmp_pub_resp, cmp_con_resp, timely_resp) values"
       "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")


def optimize_data(ro):
    for _ in se.seq:
        ro[_] = ro[_] if ro[_] != "" else "NULL"
        if len(ro[_]) > se.length[_]:
            ro[_] = ro[_][:se.length[_]+1]
    ro['complaint_id'] = int(ro['complaint_id'])

    d = dt.strptime(ro['rcv_date'], '%m/%d/%Y')
    ro['rcv_date'] = d.strftime('%Y/%m/%d')
    d = dt.strptime(ro['cmp_rcv_date'], '%m/%d/%Y')
    ro['cmp_rcv_date'] = d.strftime('%Y/%m/%d')

    ro['timely_resp'] = ro['timely_resp'][0].upper()
    ro['con_dispute'] = ro['con_dispute'][0].upper()


def read_csv(file, cur):
    with open(file, newline='') as csvfile:
        f = csv.DictReader(csvfile)
        c = 0
        for row in f:
            print(c, row)
            optimize_data(row)
            try:
                cur.execute(sql, [row[v] for v in se.seq])
                c += 1
            except Exception as e:
                print("Error - ", e)
            if c == 5:
                break
        print(c, "records inserted")


if __name__ == "__main__":
    read_csv(se.filename, conn.cursor())
    conn.commit()
    conn.close()
