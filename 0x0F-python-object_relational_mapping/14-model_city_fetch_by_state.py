#!/usr/bin/python3
"""print all city"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

conn = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
engine = create_engine(conn, pool_pre_ping=True)
Base.metadata.create_all(engine)
with Session(engine) as session:
    rows = session.query(State, City).order_by(City.id).\
            filter(State.id == City.state_id).all()
    for state, city in rows:
        print(state.name + ": " + str(city.id) + " " + city.name)
