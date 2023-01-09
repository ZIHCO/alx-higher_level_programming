#!/usr/bin/python3
"""
   This module is script that lists all values states table
   the database hbtn_0e_0_usa where name matches argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    state_name = sys.argv[4]
    c = db.cursor()
    c.execute("""SELECT * FROM states
              WHERE name LIKE BINARY '{}' \
              ORDER BY states.id ASC""".format(state_name))
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
