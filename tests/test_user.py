import pytest
from httpx import AsyncClient
from conftest import update_user


@pytest.mark.run(order=3)
async def test_get_current_user(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.get("/users/me", headers={"Cookie": f"User={token}"})
    assert response.status_code == 200


@pytest.mark.run(order=4)
@pytest.mark.usefixtures("update_user")
async def test_patch_current_user(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.patch("/users/me", json={
        "email": "something@some.com",
        "password": "root",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "Test_Patch_User",
        "telephone": "8(987)654-32-21"
    },
      headers={
          "Cookie": f"User={token}"
      })
    assert response.status_code == 200


@pytest.mark.run(order=5)
async def test_get_user_by_id(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.get(f"/users/{1}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 200

    response = await ac.get(f"/users/{3}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 404


@pytest.mark.run(order=6)
async def test_patch_user_by_id(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.patch(f"/users/{1}",
                              json={
                                  "email": "something@some.com",
                                  "password": "root",
                                  "is_active": True,
                                  "is_superuser": True,
                                  "is_verified": True,
                                  "username": "Test_Patch_User",
                                  "telephone": "8(900)600-30-20"
                              },
                              headers={"Cookie": f"User={token}"})
    assert response.status_code == 200


@pytest.mark.run(order=7)
async def test_delete_user_by_id(ac: AsyncClient):
    token = ac.cookies.get("User")

    response = await ac.post("/auth/register", json={
        "email": "s@s.com",
        "password": "oo",
        "is_active": True,
        "is_superuser": True,
        "is_verified": True,
        "username": "T",
        "telephone": "8"
    })
    assert response.status_code == 201

    response = await ac.delete(f"/users/{2}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 204
