import pytest
from httpx import AsyncClient
from sqlalchemy import select
from pizza_project.models import User
from tests.conftest import async_session_maker, user


@pytest.mark.run(order=1)
async def test_registration_user(ac: AsyncClient):
    response = await ac.post("/auth/register", json=user)
    assert response.status_code == 201

    async with async_session_maker() as session:
        query = select(
            User.email,
            User.is_active,
            User.is_superuser,
            User.is_verified,
            User.username,
            User.telephone
        )
        result = await session.execute(query)
        assert result.first() == (
            "something@some.com",
            True,
            False,
            False,
            "Test_User_1",
            "8(987)654-32-21"
        )


@pytest.mark.run(order=2)
async def test_login_user(ac: AsyncClient):
    response = await ac.post("/auth/jwt/login",
                             data={
                                 "username": "something@some.com",
                                 "password": "root",
                                 "grant_type": "password"
                             },
                             headers={
                                 "content-type": "application/x-www-form-urlencoded",
                             })
    assert response.status_code == 204


@pytest.mark.run(order=8)
async def test_logout_user(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.post("/auth/jwt/logout",
                             headers={"Cookie": f"User={token}"})
    assert response.status_code == 204
    assert ac.cookies.get("User") is None
