#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create the tables in the database based on the defined models
    Base.metadata.create_all(engine)
