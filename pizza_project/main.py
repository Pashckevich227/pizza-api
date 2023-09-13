from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database import engine, SessionLocal
from pizza_project.routers.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)


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
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response



