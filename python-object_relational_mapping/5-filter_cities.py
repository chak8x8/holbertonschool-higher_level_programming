#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # SQL injection safe query
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC", (state_name,)
    )

    # Collect cities
    cities = cur.fetchall()

    # Display comma-separated city names
    print(", ".join([city[0] for city in cities]))

    # Cleanup
    cur.close()
    db.close()
