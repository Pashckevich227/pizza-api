from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from pizza_project.routers.api import api_router

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
        request.state.db = AsyncSession()
        response = await call_next(request)
    finally:
        await request.state.db.close()
    return response




