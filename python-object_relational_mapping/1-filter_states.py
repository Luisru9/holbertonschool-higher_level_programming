#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query using format
    sql_query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
        state_name)

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
