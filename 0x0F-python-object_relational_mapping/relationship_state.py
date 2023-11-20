#!/usr/bin/python3
"""Module that defines the State model representing
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

# Create the base class
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Defines relationship between City and State models
    cities = relationship("City", backref="state", cascade="all, delete")
