#!/usr/bin/python3
"""Safely filter states from user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute(
    "SELECT * FROM states WHERE BINARY name = %s "
    "ORDER BY id ASC;",
    (state_name,)
)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
