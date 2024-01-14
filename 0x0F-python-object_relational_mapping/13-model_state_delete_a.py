#!/usr/bin/python3
"""Deletes all State object that conatains 'a' from db"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access database and delete state object"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    # Create the tables in the database based on the defined models
    Base.metadata.create_all(engine)

    # Create a sessionmaker to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all states, filtered by their state id
    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            session.delete(state)

    session.commit()

    session.close()
