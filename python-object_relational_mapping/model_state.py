#!/usr/bin/python3
"""This module defines the State class and the declarative Base.

State is mapped to the MySQL table states through SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State model mapped to the states table.

    Attributes:
        id (int): auto-generated unique primary key, never null.
        name (str): name of the state, up to 128 characters, never null.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
