from fastapi import APIRouter, Depends
from pizza_project.schemas import PizzaCreate
from pizza_project.CRUD.pizza_crud import create_pizza
from sqlalchemy.orm import Session
from pizza_project.database import get_db

router_pizza = APIRouter()


@router_pizza.get("/pizza/{id}", tags=["pizza"])
async def read_pizza(id: int):
    return {"Pizza": id}


@router_pizza.post("/pizza/", tags=["pizza"], response_model=PizzaCreate)
async def create_new_pizza(pizza: PizzaCreate, db: Session = Depends(get_db)):
    return create_pizza(db=db, pizza=pizza)