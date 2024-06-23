#!/usr/bin/python3
"""Create/save a new 'State' object"""

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

    newState = State(name="Louisiana")
    newSession.add(newState)
    newSession.commit()

    print(newState.id)

    newSession.close()
