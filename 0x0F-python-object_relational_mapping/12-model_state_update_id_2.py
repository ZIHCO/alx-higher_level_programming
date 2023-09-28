#!/usr/bin/python3
"""Update this object"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    conn = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        obj = session.query(State).filter_by(id=2).one()
        obj.name = "New Mexico"
        session.commit()
