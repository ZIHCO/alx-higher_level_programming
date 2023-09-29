#!/usr/bin/python3
"""Module containsthe class definition of a State,
   and an instance Base
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State class relational mapper"""
    from relationship_city import City
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", cascade="all, delete, delete-orphan")
