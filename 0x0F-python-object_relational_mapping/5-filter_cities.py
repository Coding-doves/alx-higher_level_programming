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

    query = "SELECT name FROM cities WHERE state_id =\
                (SELECT id FROM states WHERE name LIKE BINARY %s')\
                ORDER BY cities.id ASC"

    arg = (state_name,)
    cursor = db.cursor()

    cursor.execute(query, arg)

    cities = cursor.fetchall()

    tj = ()
    for city in cities:
        tj += city
    print(*tj, sep=", ")

    cursor.close()
    db.close()
