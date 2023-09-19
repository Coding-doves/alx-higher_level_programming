#!/usr/bin/python3
'''
import sql
'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password, db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(state_name_searched))
    
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()
