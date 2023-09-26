import pytest
import asyncio
from httpx import AsyncClient
from typing import AsyncGenerator

from sqlalchemy import update

from pizza_project.main import app
from sqlalchemy.pool import NullPool
from pizza_project.models import metadata, User
from fastapi.testclient import TestClient
from pizza_project.database import get_async_session
from config import (TEST_USER,
                    TEST_PASSWORD,
                    TEST_POSTGRES_DB,
                    TEST_POSTGRES_SERVER)
from sqlalchemy.ext.asyncio import (AsyncSession,
                                    create_async_engine,
                                    async_sessionmaker)


DATABASE_URL_TEST = f"postgresql+asyncpg://{TEST_USER}:{TEST_PASSWORD}@{TEST_POSTGRES_SERVER}/{TEST_POSTGRES_DB}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

user = {
    "email": "something@some.com",
    "password": "root",
    "is_active": True,
    "is_superuser": False,
    "is_verified": False,
    "username": "Test_User_1",
    "telephone": "8(987)654-32-21"
}

pizza = {
    "name": "Test_pizza",
    "description": "This is test pizza",
    "size": "T",
    "price": 699
}


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    app.dependency_overrides[get_async_session] = override_get_async_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def update_user() -> AsyncGenerator[AsyncClient, None]:
    async with async_session_maker() as session:
        update_data = (
            update(User)
            .where(User.email == "something@some.com")
            .values(is_superuser=True, is_verified=True)
        )
        await session.execute(update_data)
        await session.commit()
        yield session

client = TestClient(app)


