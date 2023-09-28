#!/usr/bin/python3
"""insert with orm"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    conn = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(conn, pool_pre_ping=True)
    louisiana = State(name="Louisiana")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(louisiana)
        row = session.query(State).filter(State.name.in_(["Louisiana"])).\
            first()
        print(row.id)
