#!/usr/bin/python3
'''comment'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''comment'''
    if len(sys.argv) == 4:
        '''comment'''
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database_name))

        Session = sessionmaker(bind=engine)
        session = Session()
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            '''Change the name of State with id = 2 to "New Mexico"'''
            state_to_update.name = "New Mexico"
            session.commit()
        else:
            print("State with id=2 not found")

        session.close()
