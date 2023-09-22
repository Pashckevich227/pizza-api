from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pizza_project.schemas import PizzaCreate, Pizza
from pizza_project.CRUD.pizza_crud import (create_pizza,
                                           get_pizza,
                                           get_all_pizzas,
                                           edit_pizza,
                                           delete_pizza)
from pizza_project.database import get_async_session
from pizza_project.models import User
from auth.settings import current_active_user, current_superuser

router = APIRouter()


@router.get("/pizza/{pizza_id}",
            response_model=Pizza,
            status_code=status.HTTP_200_OK)
async def read_one_pizza(pizza_id: int,
                         db: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_active_user)):
    db_pizza = await get_pizza(db, pizza_id=pizza_id)
    if db_pizza is None:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return db_pizza


@router.get("/pizza/",
            response_model=list[Pizza],
            status_code=status.HTTP_200_OK)
async def list_of_all_pizzas(skip: int = 0,
                             limit: int = 100,
                             db: AsyncSession = Depends(get_async_session),
                             user: User = Depends(current_active_user)):
    pizza = await get_all_pizzas(db=db, skip=skip, limit=limit)
    if pizza is None:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza


@router.post("/pizza/",
             response_model=PizzaCreate,
             status_code=status.HTTP_201_CREATED)
async def create_new_pizza(pizza: PizzaCreate,
                           db: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_superuser)):
    data = await create_pizza(db=db, pizza=pizza)
    return data


@router.put("/pizza/{pizza_id}", response_model=Pizza)
async def edit_one_pizza(pizza_id: int,
                         pizza: PizzaCreate,
                         db: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_superuser)):
    data = await edit_pizza(db, pizza_id=pizza_id, pizza=pizza)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Pizza not found')
    return data


@router.delete("/pizza/{pizza_id}", response_model=dict)
async def delete_one_pizza(pizza_id: int,
                           db: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_superuser)):
    data = await delete_pizza(db, pizza_id=pizza_id)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Pizza not found')
    return data
