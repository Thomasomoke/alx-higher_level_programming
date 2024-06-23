 #!/usr/bin/python3
 """
0-select_states.py module

This script connects to a MySQL database and retrieves all rows from
the 'states' table. It takes three command-line arguments: the MySQL
username, password, and database name.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
 import MySQLdb
 import sys

if __name__ == "__main__":
  db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

  c = db.cursor()
  c.execute("SELECT * FROM states")
  rows = c.fetcha11()
  for row in rows:
    print(row)
    c.close()
    db.close()

