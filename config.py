from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Переменные для БД
USER = getenv("POSTGRES_USER")
PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_SERVER = getenv("POSTGRES_SERVER")

# Переменные для тестовой БД
TEST_USER = getenv("TEST_POSTGRES_USER")
TEST_PASSWORD = getenv("TEST_POSTGRES_PASSWORD")
TEST_POSTGRES_DB = getenv("TEST_POSTGRES_DB")
TEST_POSTGRES_SERVER = getenv("TEST_POSTGRES_SERVER")

# Переменные для шифрования
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
LIFETIME = int(getenv("LIFETIME"))
SECRET_KEY_RESET_PASSWORD = getenv("SECRET_KEY_RESET_PASSWORD")
