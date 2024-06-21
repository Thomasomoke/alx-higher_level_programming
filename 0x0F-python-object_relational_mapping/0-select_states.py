#!/usr/bin/python3
#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, database_name):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to retrieve all states sorted by id
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cur.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # The script should take 3 arguments: mysql username, mysql password and database name
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
    else:
        print("Usage: ./list_states.py <mysql username> <mysql password> <database name>")

