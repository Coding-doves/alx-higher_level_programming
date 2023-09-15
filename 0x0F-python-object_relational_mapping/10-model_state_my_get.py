#!/usr/bin/python3
'''commenting'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''commenting'''
    if len(sys.argv) == 5:
        '''commenting'''
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database_name))

        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter_by(name=state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")

        session.close()
