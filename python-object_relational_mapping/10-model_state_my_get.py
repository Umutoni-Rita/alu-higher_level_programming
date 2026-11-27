#!/usr/bin/python3
"""Prints the id of the State whose name is given as argument.

Prints Not found if there is no such state. The name is sent as a
bound parameter by SQLAlchemy, so it is safe from SQL injection.
Usage: ./10-model_state_my_get.py <user> <password> <database> <state name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
