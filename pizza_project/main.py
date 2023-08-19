from fastapi import FastAPI, Depends
from models import Base
from database import engine
from routers import users_routers, pizza_routers

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(pizza_routers.router_pizza)
app.include_router(users_routers.router)


@app.get("/")
async def root():
    return {"message": "Order the Pizza!"}



