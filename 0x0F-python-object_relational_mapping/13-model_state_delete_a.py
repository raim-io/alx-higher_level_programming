#!/usr/bin/python3
"""Delete a 'State' object"""

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

    states = newSession.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        state.delete(state)

    newSession.commit()
    newSession.close()
