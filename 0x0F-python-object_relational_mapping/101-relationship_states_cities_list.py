#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using the provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create factory session
    Session = sessionmaker(bind=engine)

    # Create object session
    session = Session()

    # Retrieving states from the database and ordering them by ID
    for state in session.query(State).order_by(State.id):
        # Printing state ID and name
        print("{}: {}".format(state.id, state.name))

        # Iterating over the cities associated with the current state
        for city in state.cities:
            # Printing city ID and name
            print("    {}: {}".format(city.id, city.name))
