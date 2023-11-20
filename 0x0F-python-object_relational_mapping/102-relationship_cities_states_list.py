#!/usr/bin/python3
"""Module that retrieves and prints all cities along with
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":

    # Getting command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creating engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Creating all tables if no-existing
    Base.metadata.create_all(engine)

    # Creating configured Session class
    Session = sessionmaker(bind=engine)

    # Creating  session
    session = Session()

    # Querying all City objects and associated State objects
    cities = session.query(City).join(State).order_by(City.id)

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
