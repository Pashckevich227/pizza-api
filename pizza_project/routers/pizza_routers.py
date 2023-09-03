from fastapi import APIRouter, Depends, HTTPException, status
from pizza_project.schemas import PizzaCreate, Pizza
from pizza_project.CRUD.pizza_crud import (create_pizza,
                                           get_pizza,
                                           get_all_pizzas,
                                           edit_pizza,
                                           delete_pizza)
from sqlalchemy.orm import Session
from pizza_project.database import get_db

router_pizza = APIRouter()


@router_pizza.get("/pizza/{id}", tags=["pizza"], response_model=Pizza)
async def read_one_pizza(id: int, db: Session = Depends(get_db)):
    db_pizza = get_pizza(db, pizza_id=id)
    if db_pizza is None:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return db_pizza


@router_pizza.get("/pizza/", tags=["pizza"], response_model=list[Pizza], status_code=status.HTTP_200_OK)
async def list_of_all_pizzas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pizzas = get_all_pizzas(db=db, skip=skip, limit=limit)
    if len(pizzas) == 0:
        raise HTTPException(status_code=404, detail="Pizzas not found")
    return pizzas


@router_pizza.post("/pizza/", tags=["pizza"], response_model=PizzaCreate, status_code=status.HTTP_201_CREATED)
async def create_new_pizza(pizza: PizzaCreate, db: Session = Depends(get_db)):
    return create_pizza(db=db, pizza=pizza)


@router_pizza.put("/pizza/{id}", tags=["pizza"], response_model=Pizza)
async def edit_one_pizza(id: int, pizza: Pizza, db: Session = Depends(get_db)):
    return edit_pizza(db, pizza_id=id, pizza=pizza)


@router_pizza.delete("/pizza/{id}", tags=["pizza"], response_model=dict)
async def delete_one_pizza(id: int, db: Session = Depends(get_db)):
    return delete_pizza(db, pizza_id=id)
