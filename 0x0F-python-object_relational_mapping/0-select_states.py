#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to the MySQL server
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the query to retrieve states sorted by id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Check if the script is executed with the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, database_name)
