#!/usr/bin/python3
"""List all 'City' object by 'State'"""

from sys import argv
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    newSession = Session()

    newCity = City(name="San Francisco")
    newSate = State(name="California")
    newSate.cities.append(newCity)

    newSession.add(newCity)
    newSession.add(newSate)

    newSession.commit()
    newSession.close()
