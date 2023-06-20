#!/usr/bin/python3
"""
This module is a script that lists all the
cities from the databases hbtn_0e_4_usa.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    """
    takes 3 args: mysql username, password and
    database name
    connect to server running on localhost at port 3306
    use execute() once
    sort in ascending order
    """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    with db.cursor() as c:
        c.execute("""
                  SELECT
                      cities.id,
                  cities.name,
                      states.name
                  FROM
                      cities
                  JOIN
                      states
                  WHERE
                      state_id = states.id
                  ORDER BY cities.id ASC""")
        rows = c.fetchall()
        for row in rows:
            print(row)
