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

    cursor.execute("SELECT name FROM cities WHERE state_id =\
                (SELECT id FROM states WHERE name LIKE BINARY '{}')\
                ORDER BY cities.id ASC".format(state_name))

    cities = cursor.fetchone()

    if cities[0]:
        print(cities[0])
    else:
        print()

    cursor.close()
    db.close()
