#!/usr/bin/python3
''' import sql'''


if __name__ == "__main__":
    import MySQLdb
    import sys


    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password,
        db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name,\
                states.name FROM cities JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id ASC")
    
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
