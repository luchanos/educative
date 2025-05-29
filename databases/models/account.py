"""
Module for defining SQLAlchemy ORM models for the database.
"""

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    owner = Column(String(255), unique=True, nullable=False)
    balance = Column(Float, nullable=False)
