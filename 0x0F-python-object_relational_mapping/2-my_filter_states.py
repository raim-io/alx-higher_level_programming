#!/usr/bin/python3
"""Filter states with name starting with 'N' from the database 'hbtn_0e_0_usa'"""

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    query = """SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC""".format(sys.argv[4])
    cur = conn.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
