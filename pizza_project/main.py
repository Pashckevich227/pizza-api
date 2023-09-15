from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from database import SessionLocal
from routers import users_routers, pizza_routers


app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = AsyncSession()
        response = await call_next(request)
    finally:
        await request.state.db.close()
    return response

app.include_router(pizza_routers.router_pizza)
app.include_router(users_routers.router)


@app.get("/")
async def root():
    return {"message": "Order the Pizza!"}



