#!/usr/bin/python3
"""module contains the class City, that is object relation mapper
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class City mapper mapper"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
