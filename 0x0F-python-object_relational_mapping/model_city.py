#!/usr/bin/python3
"""
   module contains class City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class city mapper"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
