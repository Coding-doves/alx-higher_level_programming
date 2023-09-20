#!/usr/bin/python3
'''statement'''
from sqlalchemy import create_engine, select
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''statement'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(username, password, database_name),
                        pool_pre_ping=True,
                    )

    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        states = connection.execute(query)
        for state in states:
            print("{}: {}".format(state.id, state.name))

    engine.dispose()
