#!/usr/bin/python3
"""List all 'City' object by 'State'"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    newSession = Session()
    stateCities = newSession.query(
        City.id, City.name, State.name).filter(
            State.id == City.state_id
        ).order_by(City.id)

    for stateCity in stateCities:
        print(f"{stateCity[2]}: ({stateCity[0]}) {stateCity[1]}")

    newSession.close()
