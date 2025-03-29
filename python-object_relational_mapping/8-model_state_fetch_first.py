#!/usr/bin/python3
"""Prints the first State object from the database"""

# Step 1: Import required modules
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

# Step 2: Only run when the script is not imported
if __name__ == "__main__":
    # Step 3: Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Step 4: Create the database engine (connect to the DB)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    # Step 5: Create a session (used to interact with the database)
    session = Session(engine)

    # Step 6: Query for the FIRST state (ordered by ID)
    first_state = session.query(State).order_by(State.id).first()

    # Step 7: Check if we found a state, and print it
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Step 8: Close the session
    session.close()
