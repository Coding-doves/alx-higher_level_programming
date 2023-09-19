#!/usr/bin/python3
''' import sql'''
import MySQLdb
import sys

def state_list_name_matches(username, password, database_name, state_name_searched):
    '''function'''
    db = MySQLdb.connect(
                        host='localhost',
                        port=3306, user=username,
                        passwd=password, db=database_name)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name\
          LIKE BINARY '{}'ORDER BY id\
            ASC".format(state_name_searched)
    cur.execute(query, (state_name_searched,))

    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC".format(sys.argv[4])
               )    
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
        state_name_searched = sys.argv[4]
        state_list_name_matches(username, password, database_name, state_name_searched)
