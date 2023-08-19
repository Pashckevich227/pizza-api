from fastapi import APIRouter


router_pizza = APIRouter()


@router_pizza.get("/pizza/{id}", tags=["pizza"])
async def read_pizza(id: int):
    return {"Pizza": id}


