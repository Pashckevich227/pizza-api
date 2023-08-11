from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Объявляем переменные для подключения к БД
USER = getenv("POSTGRES_USER")
PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = getenv("POSTGRES_SERVER")
POSTGRES_DB = getenv("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
