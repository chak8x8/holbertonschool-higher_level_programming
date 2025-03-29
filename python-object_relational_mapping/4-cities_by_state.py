#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute query
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    # Display results
    for row in cur.fetchall():
        print(row)

    # Cleanup
    cur.close()
    db.close()
