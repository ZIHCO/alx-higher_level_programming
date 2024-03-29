#!/usr/bin/python3
"""Module containsthe class definition of a State,
   and an instance Base
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State class relational mapper"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
