#!/usr/bin/python3
"""
   This module is script that lists all states from
   the database hbtn_0e_0_usa
"""

import sys
MySQLdb = __import__('MySQLdb')

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    rows = c.fetchall()
    for row in rows:
        print(row)
