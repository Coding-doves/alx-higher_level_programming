#!/usr/bin/python3
''' import sql'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                    user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT GROUP_CONCAT(cities.name ORDER BY cities.id\
        ASC SEPARATOR ', ') FROM cities JOIN states ON cities.states_id =\
        states.id WHERE states.name = '{}'ASC".format(state_name))

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
