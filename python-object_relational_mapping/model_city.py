#!/usr/bin/python3
"""This module defines the City class mapped to the cities table.

City uses the same declarative Base as State, from model_state.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """City model mapped to the cities table.

    Attributes:
        id (int): auto-generated unique primary key, never null.
        name (str): name of the city, up to 128 characters, never null.
        state_id (int): id of the city's state, a foreign key to states.id.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
