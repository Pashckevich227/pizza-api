from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pizza_project import models, schemas


async def create_pizza(db: AsyncSession,
                       pizza: schemas.PizzaCreate):
    db_pizza = models.Pizza(
        name=pizza.name,
        description=pizza.description,
        size=pizza.size,
        price=pizza.price)
    db.add(db_pizza)
    await db.commit()
    await db.refresh(db_pizza)
    return db_pizza


async def get_pizza(db: AsyncSession,
                    pizza_id: int):
    data = select(models.Pizza).filter(models.Pizza.id == pizza_id)
    result = await db.execute(data)
    return result.scalar()


async def get_all_pizzas(db: AsyncSession,
                         skip: int = 0,
                         limit: int = 100):
    data = select(models.Pizza).offset(skip).limit(limit)
    result = await db.execute(data)
    pizzas = result.scalars().all()

    if not pizzas:
        return None

    return pizzas


async def edit_pizza(db: AsyncSession,
                     pizza_id: int,
                     pizza):
    data = await get_pizza(db, pizza_id)

    if data:
        data.name = pizza.name
        data.description = pizza.description
        data.size = pizza.size
        data.price = pizza.price

        await db.commit()
        await db.refresh(data)
        return data
    else:
        return None


async def delete_pizza(db: AsyncSession,
                       pizza_id: int):
    data = select(models.Pizza).filter(models.Pizza.id == pizza_id)
    result = await db.execute(data)
    pizza = result.scalar()
    if pizza:
        await db.delete(pizza)
        await db.commit()
        return {"massage": "Pizza deleted successfully"}
    if not pizza:
        return None
