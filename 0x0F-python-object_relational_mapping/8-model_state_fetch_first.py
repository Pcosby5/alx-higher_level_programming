#!/usr/bin/python3
"""List first State object from db"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access to db and get States from database"""
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

    # Query and print all states, ordered by their IDs
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print(state.id, state.name, sep=": ")
    else:
        print("Nothing")
