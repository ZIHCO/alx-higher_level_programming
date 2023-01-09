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
    with db.cursor() as c:
        state_name = sys.argv[4]
        c.execute("""
                SELECT
                    *
                FROM
                    states
                 WHERE
                    name
                LIKE
                    BINARY
                %(name)s
                 ORDER
                    BY
                states.id ASC
                """, {'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"'name': state_name}i
        rows = c.fetchall()
        for row in rows:
            print(row)
