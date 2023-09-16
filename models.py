import datetime as dt

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Enum, Text, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    date_created = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    last_updated = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
