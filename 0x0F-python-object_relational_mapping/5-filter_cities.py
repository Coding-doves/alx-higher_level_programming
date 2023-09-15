#!/usr/bin/python3
''' import sql'''
import MySQLdb
import sys

def cities_list(username, password, database_name, state_name):
    '''function'''
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)

    cur = db.cursor()

    query = "SELECT cities.id, cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        cities_list(username, password, database_name, state_name)
