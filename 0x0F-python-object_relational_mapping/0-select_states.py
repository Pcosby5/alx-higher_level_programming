#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306,
            user="pcosby50", passwd="root", db=database)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage:python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Extract MySQL credentials from command line arguments
        mysql_username, mysql_password, database_name = sys.argv[1:4]

        # Call the function to list states
        list_states(mysql_username, mysql_password, database_name)

