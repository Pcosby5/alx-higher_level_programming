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

    # Create a cursor object
    cur = conn.cursor()

    # Define the SQL query with a placeholder for the name filter
    sql_query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC
    """

    # Format the query with the name filter from command-line arguments
    sql_query = sql_query.format(argv[4])

    # Execute the query
    cur.execute(sql_query)

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
