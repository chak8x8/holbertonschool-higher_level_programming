#!/usr/bin/python3
"""Updates the name of the state with id=2 to 'New Mexico'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    session = Session(engine)

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
