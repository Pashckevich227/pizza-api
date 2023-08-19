from fastapi import FastAPI, Depends
from models import Base
from database import engine, SessionLocal
from routers import users_routers, pizza_routers
from pizza_project.schemas import PizzaCreate
from pizza_project.CRUD.pizza_crud import create_pizza
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(pizza_routers.router_pizza)
app.include_router(users_routers.router)


@app.get("/")
async def root():
    return {"message": "Order the Pizza!"}


@app.post("/pizza/", tags=["pizza"], response_model=PizzaCreate)
async def create_new_pizza(pizza: PizzaCreate, db: Session = Depends(get_db)):
    return create_pizza(db=db, pizza=pizza)


