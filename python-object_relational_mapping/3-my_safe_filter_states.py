#!/usr/bin/python3
"""Displays all states whose name matches the given argument.

The value is passed as a query parameter, so it is safe from SQL injection.
Usage: ./3-my_safe_filter_states.py <user> <password> <database> <name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY states.id ASC", (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
