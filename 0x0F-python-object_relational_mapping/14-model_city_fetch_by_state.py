#!/usr/bin/python3
"""prints all City objects from the db"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            state_name = session.query(State.name).filter(State.id == city.state_id).first()[0]
            print("{}: ({}) {}".format(state_name, city.id, city.name))

        session.close()
