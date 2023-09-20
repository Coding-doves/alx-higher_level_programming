#!/usr/bin/python3
'''coment'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''coment'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    session.close()
