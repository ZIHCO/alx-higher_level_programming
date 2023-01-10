#!/usr/bin/python3
"""
This module is a script that name of a state
as an argument and list all cities of the state
hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=sys.argv[1], host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as c:
        c.execute("""
                  SELECT
                      cities.name
                  FROM
                      cities
                  JOIN
                      states
                  WHERE
                      states.name
                  LIKE BINARY
                      %(name)s
                  AND
                      state_id = states.id
                  ORDER
                      BY
                  cities.id
                      ASC
                  """,
                  {'name': (sys.argv[4])})
        rows = c.fetchall()
        i = 0
        for row in rows:
            if i + 1 == len(rows):
                print(row[0], end='')
            else:
                print(row[0] + ", ", end='')
            i += 1
        print()
