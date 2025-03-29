#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get credentials from command line
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}',
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their related state
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
