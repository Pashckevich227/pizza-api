from fastapi import FastAPI, Response, Request
from models import Base
from database import engine, SessionLocal
from routers import users_routers, pizza_routers

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(pizza_routers.router_pizza)
app.include_router(users_routers.router)


@app.get("/")
async def root():
    return {"message": "Order the Pizza!"}



