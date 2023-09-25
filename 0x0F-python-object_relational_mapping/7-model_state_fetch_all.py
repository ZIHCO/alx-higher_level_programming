#!/usr/bin/python3
"""My first orm query"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    conn = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:

        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
