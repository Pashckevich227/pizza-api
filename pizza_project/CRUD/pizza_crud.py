from sqlalchemy.orm import Session
from pizza_project import models, schemas


def create_pizza(db: Session, pizza: schemas.PizzaCreate):
    db_pizza = models.Pizza(
        name=pizza.name,
        description=pizza.description,
        size=pizza.size,
        price=pizza.price)
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza


def get_pizza(db: Session, pizza_id: int):
    return db.query(models.Pizza).filter(models.Pizza.id == pizza_id).first()


def get_all_pizzas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pizza).offset(skip).limit(limit).all()
