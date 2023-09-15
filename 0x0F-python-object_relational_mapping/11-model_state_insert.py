#!/usr/bin/python3
'''commenting'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''commenting'''
    if len(sys.argv) == 4:
        '''commenting'''
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database_name))

        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)

        session.close()
