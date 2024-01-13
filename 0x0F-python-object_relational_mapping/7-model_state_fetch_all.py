#!/usr/bin/python3
"""List all states"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
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
    for state in session.query(State).order_by(State.id).all():
        print(state.id, state.name, sep=": ")

    # Close the session
    session.close()
