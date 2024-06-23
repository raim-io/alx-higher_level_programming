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

    cities = newSession.query(City).order_by(City.id)

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    newSession.close()
