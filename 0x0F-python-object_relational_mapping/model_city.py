#!/usr/bin/python3
"""
class definition of 'City' model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import (declarative_base)
from model_state import Base


class City(Base):
    """City model with 'id' and 'name' fields"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
