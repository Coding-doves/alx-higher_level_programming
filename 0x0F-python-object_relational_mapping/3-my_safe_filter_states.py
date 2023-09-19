#!/usr/bin/python3
''' import sql'''
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
                        host='localhost', port=3306,
                        user=username, passwd=password,
                        db=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
