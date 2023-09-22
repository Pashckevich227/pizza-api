import pytest
from httpx import AsyncClient
from conftest import pizza


# Create pizza
@pytest.mark.run(order=8)
async def test_create_pizza(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.post("/pizza/", json=pizza, headers={"Cookie": f"User={token}"})
    assert response.status_code == 201


@pytest.mark.run(order=8)
async def test_negative_create_pizza(ac: AsyncClient):
    token = ac.cookies.get("User")
    response = await ac.post("/pizza/",
                             json={"name": "Test_pizza"},
                             headers={"Cookie": f"User={token}"})
    assert response.status_code == 422


# Get pizza
@pytest.mark.run(order=9)
async def test_get_pizza_by_id(ac: AsyncClient):
    pizza_id = 1
    token = ac.cookies.get("User")
    response = await ac.get(f"/pizza/{pizza_id}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 200


@pytest.mark.run(order=9)
async def test_negative_get_pizza_by_id(ac: AsyncClient):
    pizza_id = 10
    token = ac.cookies.get("User")
    response = await ac.get(f"/pizza/{pizza_id}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Pizza not found'}


# Put pizza
@pytest.mark.run(order=10)
async def test_put_pizza_by_id(ac: AsyncClient):
    pizza_id = 1
    token = ac.cookies.get("User")
    response = await ac.put(f"/pizza/{pizza_id}", json={
        "name": "Test_pizza",
        "description": "Pesto",
        "size": "L",
        "price": 999
    }, headers={"Cookie": f"User={token}"})
    assert response.status_code == 200


@pytest.mark.run(order=10)
async def test_negative_put_pizza_by_id(ac: AsyncClient):
    pizza_id = 10
    token = ac.cookies.get("User")
    response = await ac.put(f"/pizza/{pizza_id}",
                            json={
                                "name": "string",
                                "description": "string",
                                "size": "S",
                                "price": 0
                            },
                            headers={"Cookie": f"User={token}"})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Pizza not found'}


# Get list pizza
@pytest.mark.run(order=11)
async def test_get_all_pizzas(ac: AsyncClient):
    await test_create_pizza(ac)
    skip = 0
    limit = 100
    token = ac.cookies.get("User")
    response = await ac.get(f"/pizza/?skip={skip}&limit={limit}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.run(order=11)
async def test_negative_get_all_pizzas(ac: AsyncClient):
    await test_create_pizza(ac)
    skip = 0
    limit = 0
    token = ac.cookies.get("User")
    response = await ac.get(f"/pizza/?skip={skip}&limit={limit}", headers={"Cookie": f"User={token}"})

    assert response.status_code == 404
    assert response.json() == {'detail': 'Pizza not found'}


# Delete pizza
@pytest.mark.run(order=12)
async def test_delete_pizza_by_id(ac: AsyncClient):
    pizza_id = 2
    token = ac.cookies.get("User")
    response = await ac.delete(f"/pizza/{pizza_id}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 200


@pytest.mark.run(order=12)
async def test_negative_delete_pizza_by_id(ac: AsyncClient):
    pizza_id = 10
    token = ac.cookies.get("User")
    response = await ac.delete(f"/pizza/{pizza_id}", headers={"Cookie": f"User={token}"})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Pizza not found'}

