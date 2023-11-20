#!/usr/bin/python3
"""Module that defines the City model representing
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class
Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
