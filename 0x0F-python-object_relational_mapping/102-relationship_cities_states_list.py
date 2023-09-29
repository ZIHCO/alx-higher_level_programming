#!/usr/bin/python3
"""create an object"""
from sqlalchemy import create_engine
from sys import argv
from relationship_state import State, Base
from sqlalchemy.orm import Session
from relationship_city import City

if __name__ == "__main__":
    conn = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        cities = session.query(City, State).filter(State.id == City.state_id).\
                all()
        for city, state in cities:
            print(str(city.id) + ": " + city.name + " -> " + state.name)
