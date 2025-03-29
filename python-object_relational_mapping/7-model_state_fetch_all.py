#!/usr/bin/python3
"""Lists all State objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Step 1: Get credentials from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Step 2: Create engine (connection to MySQL)
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )


    # Step 3: Create session to interact with the database
    session = Session(engine)

    # Step 4: Query all states ordered by ID
    states = session.query(State).order_by(State.id).all()

    # Step 5: Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Step 6: Close the session
    session.close()
