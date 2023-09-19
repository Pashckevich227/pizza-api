import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Text,
                        Float,
                        MetaData,
                        TIMESTAMP,
                        Boolean)


metadata = MetaData()


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(length=30), default=False, nullable=False)
    telephone: Mapped[str] = mapped_column(String(length=30), default=False, nullable=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow())
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class Pizza(Base):
    __tablename__ = "pizza"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    size = Column(String(1), nullable=False)
    price = Column(Float, nullable=False)
