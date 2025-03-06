#!/usr/bin/python3

"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    root_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                                format(
                                    sys.argv[1], sys.argv[2], sys.argv[3]),
                                pool_pre_ping=True)

    session = sessionmaker(bind=root_engine)()
    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
