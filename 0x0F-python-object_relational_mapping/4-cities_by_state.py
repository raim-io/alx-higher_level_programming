#!/usr/bin/python3
"""Filter states with name starting with 'N'
from the database 'hbtn_0e_0_usa'
and avoid SQL injections"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""
                SELECT
                    cities.id, cities.name, states.name
                FROM cities
                JOIN states ON states.id = cities.state_id ORDER BY id ASC
                """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
