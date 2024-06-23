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

    state = newSession.query(
        State).order_by(State.id).filter_by(name = argv[4]).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print('Not found')

    newSession.close()
