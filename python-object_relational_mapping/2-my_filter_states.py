#!/usr/bin/python3
"""Displays all states whose name matches the given argument.

The query is built with format(), so it is NOT safe from SQL injection.
Usage: ./2-my_filter_states.py <user> <password> <database> <state name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
             "ORDER BY states.id ASC").format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
