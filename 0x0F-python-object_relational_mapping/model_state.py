#!/usr/bin/python3
"""
class definition of 'State' model
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import (declarative_base)

stateMetadata = MetaData()
Base = declarative_base(metadata=stateMetadata)


class State(Base):
    """State model with 'id' and 'name' fields"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False, )
