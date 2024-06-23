#!/usr/bin/python3
"""List all 'State' object"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    newSession = Session()

    states = newSession.query(
        State).order_by(State.id).filter(State.name.like('%a%'))
    for state in states:
        print(f"{state.id}: {state.name}")

    newSession.close()
