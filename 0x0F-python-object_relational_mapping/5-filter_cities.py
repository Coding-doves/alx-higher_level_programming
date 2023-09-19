#!/usr/bin/python3
''' import sql'''


def cities_list(username, password, database_name, state_name):
    '''function'''
    db = MySQLdb.connect(host='localhost', port=3306,
                    user=username, passwd=password, db=database_name)

    cur = db.cursor()

    cur.execute("SELECT GROUP_CONCAT(cities.name ORDER BY cities.id\
        ASC SEPARATOR ', ') FROM cities JOIN states ON cities.states_id =\
        states.id WHERE states.name = '{}'ASC".format(state_name))

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    import sys


    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        cities_list(username, password, database_name, state_name)
