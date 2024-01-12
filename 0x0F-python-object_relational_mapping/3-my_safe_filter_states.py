#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor to execute SQL queries
    cur = conn.cursor()

    # Execute a parameterized query to retrieve states with a specific name
    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
            (argv[4],)
    )

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
