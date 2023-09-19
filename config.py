from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Переменные для БД
USER = getenv("POSTGRES_USER")
PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_SERVER = getenv("POSTGRES_SERVER")

# Переменные для шифрования
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
LIFETIME = int(getenv("LIFETIME"))
SECRET_KEY_RESET_PASSWORD = getenv("SECRET_KEY_RESET_PASSWORD")
