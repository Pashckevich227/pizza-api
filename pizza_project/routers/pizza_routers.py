from fastapi import APIRouter, Depends, HTTPException
from pizza_project.schemas import PizzaCreate, Pizza
from pizza_project.CRUD.pizza_crud import (create_pizza,
                                           get_pizza,
                                           get_all_pizzas)
from sqlalchemy.orm import Session
from pizza_project.database import get_db

router_pizza = APIRouter()


@router_pizza.get("/pizza/{id}", tags=["pizza"], response_model=Pizza)
async def read_pizza(id: int, db: Session = Depends(get_db)):
    db_pizza = get_pizza(db, pizza_id=id)
    if db_pizza is None:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return db_pizza


@router_pizza.get("/pizza/", tags=["pizza"], response_model=list[Pizza])
async def list_of_all_pizzas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pizzas = get_all_pizzas(db=db, skip=skip, limit=limit)
    if len(pizzas) == 0:
        raise HTTPException(status_code=404, detail="Pizzas not found")
    return pizzas


@router_pizza.post("/pizza/", tags=["pizza"], response_model=PizzaCreate)
async def create_new_pizza(pizza: PizzaCreate, db: Session = Depends(get_db)):
    return create_pizza(db=db, pizza=pizza)
