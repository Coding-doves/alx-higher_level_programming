#!/usr/bin/python3
''' import sql'''
import MySQLdb
import sys


def state_list_name_N(username, password, database_name):
    '''function'''
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_list_name_N(username, password, database_name)
