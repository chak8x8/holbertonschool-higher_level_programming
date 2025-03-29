#!/usr/bin/python3
"""
Lists all states with a name matching the user input
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cur = db.cursor()

    # Correct query + call execute()
    query = "SELECT * FROM states WHERE BINARY = '{}' " \
        "ORDER BY id ASC;".format(state_name)
    cur.execute(query)

    # Correct fetchall()
    for row in cur.fetchall():
        print(row)

    # Cleanup
    cur.close()
    db.close()
