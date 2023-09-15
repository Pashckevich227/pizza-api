import datetime
from database import Base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Text,
                        Float,
                        Table,
                        MetaData,
                        TIMESTAMP,
                        Boolean)

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(length=320), unique=True, index=True, nullable=False),
    Column("telephone", String(length=30), default=False, nullable=True),
    Column("username", String(length=30), default=False, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.datetime.utcnow),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

# pizza = Table(
#     "pizza",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(length=30), nullable=False),
#     Column("description", Text),
#     Column("size", String(length=1), nullable=False),
#     Column("price", Float, nullable=False)
# )


class Pizza(Base):
    __tablename__ = "pizza"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    size = Column(String(1), nullable=False)
    price = Column(Float, nullable=False)
