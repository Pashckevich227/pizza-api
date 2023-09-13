from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Переменные для БД
USER = getenv("POSTGRES_USER")
PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_SERVER = getenv("POSTGRES_SERVER")

# Переменные для OAUTH2
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))