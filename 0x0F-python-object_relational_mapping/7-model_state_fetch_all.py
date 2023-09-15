#!/usr/bin/python3
'''statement'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''statement'''
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database_name))

        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))

        session.close()
