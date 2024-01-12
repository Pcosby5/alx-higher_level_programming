#!/usr/bin/python3
"""Lists cities of a specific state"""

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

    # Execute a parameterized query to retrieve cities of a specific state
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (argv[4],))

    # Print the names of cities, joined by commas
    print(", ".join(map(lambda x: x[0], cur.fetchall())))

    # Close the cursor and connection
    cur.close()
    conn.close()
