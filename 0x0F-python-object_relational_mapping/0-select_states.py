#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        c = db.cursor()
        c.execute("SELECT * FROM states")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if c:
            c.close()
        if db:
            db.close()

