#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials arguments
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    y = db.cursor()

    # Execute the SQL query
    y.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in y.fetchall() if state[1][0] == "N"]
