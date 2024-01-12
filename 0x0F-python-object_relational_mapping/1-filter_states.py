#!/usr/bin/python3
"""List of states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to MySQL server
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()
