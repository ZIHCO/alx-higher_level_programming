#!/usr/bin/python3
"""
   Write a Python file similar to model_state.py named model_city.py
   that contains the class definition of a City.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class City mapper mapper"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
