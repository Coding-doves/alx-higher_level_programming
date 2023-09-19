#!/usr/bin/python3
''' import sql'''
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password, db=database_name
        )

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name,\
                state.name FROM cities JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
