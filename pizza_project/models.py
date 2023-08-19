from database import Base

from sqlalchemy import (Column,
                        Integer,
                        String,
                        Text,
                        Float)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    telephone = Column(String(30))
    city = Column(String(30))
    street = Column(String(100))
    house = Column(Integer)
    room = Column(Integer)


class Pizza(Base):
    __tablename__ = "pizza"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    size = Column(String(1), nullable=False)
    price = Column(Float, nullable=False)

