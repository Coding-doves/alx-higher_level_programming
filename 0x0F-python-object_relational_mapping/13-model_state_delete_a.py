#!/usr/bin/python3
'''comment'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''comment'''
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        '''comment'''
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database_name))

        Session = sessionmaker(bind=engine)
        session = Session()
        states_with_a = session.query(State).filter(State.name.like("%a%")).all()

        for state in states_with_a:
            session.delete(state)

        session.commit()

        session.close()
