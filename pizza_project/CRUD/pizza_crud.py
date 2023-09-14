from sqlalchemy.orm import Session

from pizza_project.database import get_async_session
from pizza_project import models, schemas
from fastapi import HTTPException, status


def create_pizza(db: get_async_session, pizza: schemas.PizzaCreate):
    db_pizza = models.pizza(
        name=pizza.name,
        description=pizza.description,
        size=pizza.size,
        price=pizza.price)
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza


def get_pizza(db: Session, pizza_id: int):
    return db.get(models.pizza, pizza_id)


def get_all_pizzas(db: get_async_session, skip: int = 0, limit: int = 100):
    return db.query(models.pizza).offset(skip).limit(limit).all()


def edit_pizza(db: get_async_session, pizza_id: int, pizza):
    db_pizza = db.query(models.pizza).filter(models.pizza.id == pizza_id).first()

    if db_pizza:
        for attr, value in pizza.model_dump().items():
            setattr(db_pizza, attr, value)

        db.commit()
        db.refresh(db_pizza)
        return db_pizza
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Pizza not found')


def delete_pizza(db: get_async_session, pizza_id: int):
    db_pizza = db.query(models.pizza).filter(models.pizza.id == pizza_id).first()

    if db_pizza:
        db.delete(db_pizza)
        db.commit()
        return {"massage": "Pizza deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Pizza not found')

